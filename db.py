import sqlite3
import os
import util
from config import Config


class DB_Connector:
    __instance = None

    @staticmethod
    def getInstance(db_name="dns.db"):
        """ Static access method """
        if DB_Connector.__instance is None:
            DB_Connector(db_name)
        return DB_Connector.__instance

    def __init__(self, db_name="dns.db"):
        """Constructor"""
        if DB_Connector.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DB_Connector.__instance = self
            self.connection = sqlite3.connect(db_name)
            self.initialise()

    def initialise(self):
        """Initialises the tables of the database"""
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        c = self.connection.cursor()
        for file in os.listdir(ROOT_DIR + '/sql'):
            if file.endswith('.sql'):
                qry = open(ROOT_DIR + os.path.join("/sql", file), 'r').read()
                c.execute(qry)
        self.connection.commit()
        c.close()

    def execute_query(self, qry):
        """Executes a query"""
        c = self.connection.cursor()
        c.execute(qry)
        c.close()

    def fetch(self, qry):
        """Fetches data based on query"""
        c = self.connection.cursor()
        result = c.execute(qry).fetchone()
        c.close()
        return result

    def fetchAll(self, qry):
        """Fetch all data based on query"""
        c = self.connection.cursor()
        result = c.execute(qry).fetchall()
        c.close()
        return result

    ### Start of domain section ###

    def hasDomain(self, name: str):
        """Returns True if the given domain-name exists in the database"""
        return self.getDomainId(name) is not None

    def addDomain(self, domain_name: str):
        """Adds the given domain-name to database"""
        now = util.now()
        qry = 'INSERT INTO domains (name, created_at, updated_at) VALUES ("%s", "%s", "%s")' % (domain_name, now, now)
        self.execute_query(qry)
        self.connection.commit()

    def getDomainId(self, name: str):
        """Returns domain-id of the given name"""
        qry = 'SELECT id FROM domains where name LIKE "%s"' % name
        return self.fetch(qry)

    def getDomain(self, domain_id):
        """Returns the domain-name"""
        qry = "SELECT name FROM domains where id = %d" % domain_id
        return self.fetch(qry)

    def getAllDomains(self):
        """Returns all entrys in domain-table"""
        qry = "SELECT * FROM domains"
        return self.fetchAll(qry)

    ### Start of server section ###

    def hasServer(self, name: str):
        """Returns True if the given server-name exists in the database"""
        return self.getServerID(name) is not None

    def addServer(self, server_name: str):
        """Adds the given ip to database"""
        now = util.now()
        qry = 'INSERT INTO server (ip, created_at, updated_at) VALUES ("%s", "%s", "%s")' % (server_name, now, now)
        self.execute_query(qry)
        self.connection.commit()

    def getServerID(self, name: str):
        """Returns server-id of the given name"""
        qry = 'SELECT id FROM server where ip LIKE "%s"' % name
        return self.fetch(qry)

    def getServer(self, server_id):
        """Returns the server-name"""
        qry = "SELECT ip FROM server where id = %d" % server_id
        return self.fetch(qry)

    def getAllServer(self):
        """Returns all entrys in server-table"""
        qry = "SELECT * FROM server"
        return self.fetchAll(qry)

    ### Start of request section ###

    def addRequest(self, domain: str, dnsServer: str, ip="", mac=""):
        if not self.hasDomain(domain):
            self.addDomain(domain)
        domain_id = self.getDomainId(domain)[0]
        if not self.hasServer(dnsServer):
            self.addServer(dnsServer)
        server_id = self.getServerID(dnsServer)[0]
        now = util.now()
        qry = 'INSERT INTO requests (ip, mac, domain_name, server, created_at, updated_at) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % (
            ip, mac, domain_id, server_id, now, now)
        self.execute_query(qry)
        self.connection.commit()

    def getAllRequests(self):
        """Returns all entrys in request-table"""
        qry = "SELECT * FROM requests"
        return self.fetchAll(qry)

    def getRequestsBy(self, key, value):
        """Returns all entrys in request-table where key is like value"""
        qry = 'SELECT * FROM requests WHERE (%s) LIKE ("%s")' % (key, value)
        return self.fetchAll(qry)

    def getTopTenDomains(self):
        if len(Config.excluded_domains) is 0:
            qry = 'SELECT d.name, COUNT(r.domain_name) as count FROM requests r, domains d WHERE r.domain_name = d.id GROUP BY d.name ORDER BY COUNT(r.domain_name) DESC'
        else:
            filter = '(%s)' % ', '.join(['"' + str(i) + '"' for i in Config.excluded_domains])
            qry = "SELECT d.name, COUNT(r.domain_name) as count FROM requests r, domains d WHERE r.domain_name = d.id AND d.name NOT IN %s GROUP BY d.name ORDER BY COUNT(r.domain_name) DESC" % filter
        result = self.fetchAll(qry)
        return result[0:min(10, len(result))]

    def getTopTenDNSServer(self):
        qry = 'SELECT s.ip, COUNT(r.server) as count FROM requests r, server s WHERE r.server = s.id GROUP BY s.ip ORDER BY COUNT(r.server) DESC'
        result = self.fetchAll(qry)
        return result[0:min(10, len(result))]

    def requestCount(self):
        if len(Config.excluded_domains) is 0:
            qry = 'SELECT COUNT(*) FROM requests'
        else:
            _filter = '(%s)' % ', '.join(['"' + str(i) + '"' for i in Config.excluded_domains])
            qry = 'SELECT COUNT(*) FROM requests WHERE domain_name NOT IN (SELECT id FROM domains WHERE name IN %s)' % _filter
        print(self.fetch(qry)[0])
        return self.fetch(qry)[0]

    def DNSCount(self):
        qry = 'SELECT COUNT(*) FROM server'
        return self.fetch(qry)[0]


if __name__ == '__main__':
    dbc = DB_Connector()
    dbc.initialise()
    print(dbc.requestCount())
