import matplotlib.pyplot as plt
from db import DB_Connector


def showTopTenDomains():
    """Creates a pie chart with the top ten domains"""
    labels, sizes = __getTopTenDomains()
    __show(labels, sizes)


def showTopTopDNSServer():
    """Creates a pie chart with the top ten DNS-server"""
    labels, sizes = __getTopTenDNSServer()
    __show(labels, sizes)


def __show(labels, sizes):
    """Visualise the given data in a pie chart """
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.show()


def plotAllInOne():
    # Count of all requests in the Database
    countOfRequests = DB_Connector.getInstance().requestCount()

    # Get names and counts of the top ten domains
    lables_domain, sizes_domain = __getTopTenDomains()

    # Creation of lists to show "Other" domains in relation to the top ten
    labels_domain_other, sizes_domain_other = lables_domain.copy(), sizes_domain.copy()
    labels_domain_other.append("Other")
    sizes_domain_other.append(countOfRequests - sum(sizes_domain))

    # Now the DNS-server:
    lables_dns, sizes_dns = __getTopTenDNSServer()

    # And with other:
    lables_dns_other, sizes_dns_other = lables_domain.copy(), sizes_domain.copy()
    lables_dns_other.append("Other")
    sizes_dns_other.append(countOfRequests - sum(sizes_dns))

    # Now its time to visualise it
    f, axarr = plt.subplots(2, 2)
    __createSubplot(axarr[0, 0], lables_domain, sizes_domain, "Top ten Domains")
    __createSubplot(axarr[1, 0], labels_domain_other, sizes_domain_other,
                    "Top ten Domains with \"other\"")
    __createSubplot(axarr[0, 1], lables_dns, sizes_dns, "Top ten DNS-Server")
    __createSubplot(axarr[1, 1], lables_dns, sizes_dns, "Top ten DNS-Server with \"other\"")
    plt.show()


def __createSubplot(ax, labels, sizes, title=""):
    """ Creates a new pie chart in the given plot"""
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)


def __getTopTenDomains():
    """Returns two lists with the names and counts of the top ten domains"""
    dbc = DB_Connector.getInstance()
    labels, sizes = [], []
    for domain in dbc.getTopTenDomains():
        labels.append(domain[0])
        sizes.append(domain[1])
    return labels, sizes


def __getTopTenDNSServer():
    dbc = DB_Connector.getInstance()
    labels, sizes = [], []
    for server in dbc.getTopTenDNSServer():
        labels.append(server[0])
        sizes.append(server[1])
    return labels, sizes


if __name__ == '__main__':
    # showTopTenDomains()
    # showTopTopDNSServer()
    plotAllInOne()
