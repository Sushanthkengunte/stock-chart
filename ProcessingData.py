
import mpld3
from mpld3 import plugins





stocks = {"Apple":"EOD/AAPL",
          "Microsoft":"EOD/MSFT",
          "Ebay":"EOD/EBAY",
          "Walmart":"EOD/WMT",
          "Tableau":"EOD/DATA",
          "Disney":"EOD/DIS"
          }



def filterData(dataset,startYear,endYear,priceType='Open'):
    prices = dataset[priceType]
    return prices.loc[startYear:endYear]




def calculateMovingAverages(stockPrices):
    lastTenAverage = list()
    for i in range(len(stockPrices)):
        lastTenAverage.append(((sum(stockPrices[max(0, i - 10):i])) / (1 if (i - max(0, i - 10)) == 0 else (i - max(0, i - 10)))))
    movingAverage = []
    for i,dt in enumerate(lastTenAverage):
        dt = "{0:.3f}".format(dt)
        movingAverage.append('Moving Average: '+str(dt) +'<br/> Current price: ' + str(stockPrices[i]))

    return movingAverage



def generateChart(companyName,data):

    fig, ax = plt.subplots(figsize=(8, 5))

    stockPrices = data.values
    movingAverage = calculateMovingAverages(stockPrices)

    lines = plt.plot(data.index, stockPrices, marker='o', ls='-', ms=5, markerfacecolor='None',markeredgecolor='None', )

    ax.set_xlabel('year')
    ax.set_ylabel('Open prices')
    ax.set_title('Stock chart of '+companyName, size=20)

    tooltip = plugins.PointHTMLTooltip(lines[0], movingAverage, voffset=10, hoffset=10)
    plugins.connect(fig, tooltip)

    return mpld3.fig_to_html(fig)


dataset = None
prevCompany = None
