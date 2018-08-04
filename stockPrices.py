from flask import Flask, render_template, request
import api
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()

from threading import Lock
lock = Lock()

import mpld3
from mpld3 import plugins

import json



app = Flask(__name__)



stocks = {"Apple":"EOD/AAPL",
            "something":"CODE"
          }


@app.route("/")
def index():
    return render_template("index.html")





@app.route("/stockChart",methods=['POST'])
def convertDataToChart():
    data = json.loads(request.data)
    companyName = data['companyName']
    if data != None and companyName in stocks.keys():
        companyCode = stocks[companyName]
        data = api.getData(companyCode)
        htmlFormOfGraph = generateChart(data,companyName)
        return htmlFormOfGraph
    else:
        return '<script type="text/javascript">alert("Something went wrong while sending the request or getting the company name, Please try again");</script>'





def generateChart(data,companyName):

    fig, ax = plt.subplots(figsize=(10, 6))

    stockPrices = data['Open'].values
    lastTenAverage = list()
    for i in range(len(stockPrices)):
        lastTenAverage.append((sum(stockPrices[max(0, i - 10):i])) / (1 if (i - max(0, i - 10)) == 0 else (i - max(0, i - 10))))

    movingAverage = []
    for i,dt in enumerate(lastTenAverage):
        movingAverage.append('Moving Average: '+str(dt) +'<br/> Current price: ' + str(stockPrices[i]))

    lines = plt.plot(data.index, stockPrices, marker='o', ls='-', ms=5, markerfacecolor='None',markeredgecolor='None', )

    ax.set_xlabel('year')
    ax.set_ylabel('Open prices')
    ax.set_title('Stock chart of '+companyName, size=20)

    tooltip = plugins.PointHTMLTooltip(lines[0], movingAverage, voffset=10, hoffset=10)
    plugins.connect(fig, tooltip)

    return mpld3.fig_to_html(fig)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777)