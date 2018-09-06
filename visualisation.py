import matplotlib.pyplot as plt
from db import DB_Connector


def showTopTenDomains():
    dbc = DB_Connector.getInstance()
    labels, sizes = [], []
    for domain in dbc.getTopTenDomains():
        labels.append(domain[0])
        sizes.append(domain[1])
    __show(labels, sizes)


def showTopTopDNSServer():
    dbc = DB_Connector.getInstance()
    labels, sizes = [], []
    for domain in dbc.getTopTenDNSServer():
        labels.append(domain[0])
        sizes.append(domain[1])
    __show(labels, sizes)


def __show(labels, sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


if __name__ == '__main__':
    showTopTenDomains()
    showTopTopDNSServer()
