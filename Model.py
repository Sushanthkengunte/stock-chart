import quandl

# include the api config api key as quandl.ApiConfig.api_key = "*******"


stockMetaData = {"Apple":"EOD/AAPL",
          "Microsoft":"EOD/MSFT",
          "Ebay":"EOD/EBAY",
          "Walmart":"EOD/WMT",
          "Tableau":"EOD/DATA",
          "Disney":"EOD/DIS"
          }


# get the data using the company code.
def getData(companyName):
    companyCode = stockMetaData[companyName]
    return quandl.get(companyCode)




# filter data between the year range ( extendable to use other type of prices)
def filterData(dataset,startYear,endYear,priceType='Open'):
    prices = dataset[priceType]
    return prices.loc[startYear:endYear]




def calcMovingAvg(stockPrices,factor):
    '''
    Calculate the moving average of the last 10 or less stock pricces
    :param stockPrices: prices
    :param factor: how many of the previous number of values to consider for average
    :return: list of moving average
    '''
    lastTenAverage = list()

    #calculating average
    for i in range(len(stockPrices)):
        lastTenAverage.append(((sum(stockPrices[max(0, i - factor):i])) / (1 if (i - max(0, i - factor)) == 0 else (i - max(0, i - factor)))))

    return lastTenAverage

def crtLabelMovingAverage(lastTenAverage,stockPrices):
    '''
        Creates labels for averages
    :param lastTenAverage: the averages of the last 10 or less stock pricces
    :param stockPrices: open prices
    :return: labels with moving average and open price
    '''
    movingAverage = []
    for i,dt in enumerate(lastTenAverage):
        dt = "{0:.3f}".format(dt)
        movingAverage.append('Moving Average: '+str(dt) +'<br/> Current price: ' + str(stockPrices[i]))

    return movingAverage