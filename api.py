import quandl


def getData(companyCode):
    return quandl.get(companyCode)