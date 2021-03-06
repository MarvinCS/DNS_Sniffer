import matplotlib.pyplot as plt
from db import Connection_handler


class Pie_Chart:
    """This class contains methods to generate pie-charts based on matplotlib"""

    @staticmethod
    def showTopTenDomains():
        """Creates a pie chart with the top ten domains"""
        labels, sizes = Pie_Chart.__getTopTenDomains()
        Pie_Chart.__show(labels, sizes)

    @staticmethod
    def showTopTopDNSServer():
        """Creates a pie chart with the top ten DNS-server"""
        labels, sizes = Pie_Chart.__getTopTenDNSServer()
        Pie_Chart.__show(labels, sizes)

    @staticmethod
    def __show(labels, sizes):
        """Visualise the given data in a pie chart """
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()

    @staticmethod
    def plotAllInOne():
        """Plots four pie-charts. Two with domain-counts and two with dns-counts"""
        # Count of all requests in the Database
        countOfRequests = Connection_handler.getConnection().requestCount()

        # Get names and counts of the top ten domains
        lables_domain, sizes_domain = Pie_Chart.__getTopTenDomains()

        # Creation of lists to show "Other" domains in relation to the top ten
        labels_domain_other, sizes_domain_other = lables_domain.copy(), sizes_domain.copy()
        labels_domain_other.append("Other")
        sizes_domain_other.append(countOfRequests - sum(sizes_domain))

        # Now the DNS-server:
        lables_dns, sizes_dns = Pie_Chart.__getTopTenDNSServer()

        # And with other:
        lables_dns_other, sizes_dns_other = lables_domain.copy(), sizes_domain.copy()
        lables_dns_other.append("Other")
        sizes_dns_other.append(countOfRequests - sum(sizes_dns))

        # Now its time to visualise it
        f, axarr = plt.subplots(2, 2)
        Pie_Chart.__createSubplot(axarr[0, 0], lables_domain, sizes_domain, "Top ten Domains")
        Pie_Chart.__createSubplot(axarr[1, 0], labels_domain_other, sizes_domain_other,
                                  "Top ten Domains with \"other\"")
        Pie_Chart.__createSubplot(axarr[0, 1], lables_dns, sizes_dns, "Top ten DNS-Server")
        Pie_Chart.__createSubplot(axarr[1, 1], lables_dns, sizes_dns, "Top ten DNS-Server with \"other\"")
        plt.show()

    @staticmethod
    def __createSubplot(ax, labels, sizes, title=""):
        """ Creates a new pie chart in the given plot"""
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title(title)

    @staticmethod
    def __getTopTenDomains():
        """Returns two lists with the names and counts of the top ten domains"""
        dbc = Connection_handler.getConnection()
        labels, sizes = [], []
        for domain in dbc.getTopTenDomains():
            labels.append(domain[0])
            sizes.append(domain[1])
        return labels, sizes

    @staticmethod
    def __getTopTenDNSServer():
        """Returns two lists with the names and counts of the top ten dns-server"""
        dbc = Connection_handler.getConnection()
        labels, sizes = [], []
        for server in dbc.getTopTenDNSServer():
            labels.append(server[0])
            sizes.append(server[1])
        return labels, sizes


if __name__ == '__main__':
    # showTopTenDomains()
    # showTopTopDNSServer()
    Pie_Chart.plotAllInOne()
