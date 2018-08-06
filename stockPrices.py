from flask import Flask, render_template, request

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()


from threading import Lock
lock = Lock()



import mpld3
from mpld3 import plugins
import json


import Model


def generateChart(companyName,data):
    '''
        Use the data to calculate moving average and plot chart using moving average as label
    :param companyName: Name of the company
    :param data: stock prices
    :return: return chart in html
    '''

    fig, ax = plt.subplots(figsize=(8, 5))

    stockPrices = data.values
    movingAverageValues = Model.calcMovingAvg(stockPrices,10)
    movingAverage = Model.crtLabelMovingAverage(movingAverageValues,stockPrices)

    stockPricePoints = plt.plot(data.index, stockPrices, marker='o', ls='-', ms=5, markerfacecolor='None',markeredgecolor='None', )

    ax.set_xlabel('year')
    ax.set_ylabel('Open prices')
    ax.set_title('Stock chart of '+companyName, size=20)

    tooltip = plugins.PointHTMLTooltip(stockPricePoints[0], movingAverage, voffset=10, hoffset=10)
    plugins.connect(fig, tooltip)

    return mpld3.fig_to_html(fig)


# pseudoDatabase
dataset = None
prevCompany = None




app = Flask(__name__)

#Routes
@app.route("/")
def index():
    return render_template("index.html")





@app.route("/stockChart",methods=['POST'])
def convertDataFromApiToChart():
    '''
        requests data from using api and returns a stock chart
    :return: html string for the stock chart
    '''

    #load data from front end
    data = json.loads(request.data)

    global prevCompany

    #get parameters from view
    companyName = data['companyName']
    startYear = data['startYear']
    endYear = data['endYear']


    global dataset
    try:
        # check if data for the company has to be downloaded
        if dataset is None or prevCompany != companyName:
            dataset = Model.getData(companyName)
        prevCompany = companyName
        filteredData = Model.filterData(dataset, startYear, endYear)
        htmlFormOfGraph = generateChart(companyName, filteredData)
    except Exception as error:
        return str(error)
    else:
        return htmlFormOfGraph





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777)