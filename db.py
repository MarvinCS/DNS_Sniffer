import sqlite3
import os


class DB_Connector:
    __instance = None

    @staticmethod
    def getInstance(db_name="dns.db"):
        """ Static access method """
        if DB_Connector.__instance is None:
            DB_Connector(db_name)
        return DB_Connector.__instance

    def __init__(self, db_name="dns.db"):
        if DB_Connector.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DB_Connector.__instance = self
            self.connection = sqlite3.connect(db_name)
            self.initialise()

    def initialise(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        c = self.connection.cursor()
        for file in os.listdir(ROOT_DIR + '/sql'):
            if file.endswith('.sql'):
                qry = open(ROOT_DIR + os.path.join("/sql", file), 'r').read()
                c.execute(qry)
        self.connection.commit()
        c.close()

    ### Start of domain section ###

    def hasDomain(self, name: str):
        return self.getDomainId(name) is not None

    def addDomain(self, domain_name: str):
        qry = "INSERT INTO domains (name) VALUES (\"%s\")" % domain_name
        print(qry)
        c = self.connection.cursor()
        c.execute(qry)
        self.connection.commit()
        c.close()

    def getDomainId(self, name: str):
        qry = "SELECT id FROM domains where name LIKE \"%s\"" % name
        c = self.connection.cursor()
        domain_id = c.execute(qry).fetchone()
        c.close()
        return domain_id

    def getDomain(self, domain_id):
        qry = "SELECT name FROM domains where id = %d" % domain_id
        c = self.connection.cursor()
        name = c.execute(qry).fetchone()
        c.close()
        return name

    ### Start of server section ###


if __name__ == '__main__':
    db_connector = DB_Connector.getInstance()
    db_connector.initialise()
