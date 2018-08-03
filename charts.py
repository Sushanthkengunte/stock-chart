from flask import Flask, flash, redirect, render_template, request, session, abort
import quandl
import matplotlib.pyplot as plt
import matplotlib
import mpld3
from mpld3 import plugins,utils




app = Flask(__name__)

# stocks = [{"id": 0, "name": "Apple"}, {"id": 1, "name": "something"}]

stocks = [{"name": "Apple","code":"EOD/AAPL"}, {"name": "something","code":"CODE"}]


@app.route("/")
def index():
    return render_template("index.html",stocks=stocks)





@app.route("/<string:id>/")
def stockChart(id):
    index = int(float(id))
    htmlFormOfGraph = getHtml(index-1)
    return render_template("display.html",plot = htmlFormOfGraph)
    # return htmlFormOfGraph


def getHtml(id):
    stockMetaData = stocks[id]
    data = quandl.get(stockMetaData.get("code"))


    fig, ax = plt.subplots(figsize=(10, 6))

    movingAverage = data['Open'].values
    average = list()
    for i in range(len(movingAverage)):
        average.append(
            (sum(movingAverage[max(0, i - 10):i])) / (1 if (i - max(0, i - 10)) == 0 else (i - max(0, i - 10))))

    labels = []
    for dt in average:
        labels.append(str(dt))

    lines = plt.plot(data.index, movingAverage, marker='o', ls='-', ms=5, markerfacecolor='None',
                     markeredgecolor='None', )

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Stock chart', size=20)

    tooltip = plugins.PointHTMLTooltip(lines[0], labels, voffset=10, hoffset=10)
    plugins.connect(fig, tooltip)
    # mpld3.show()
    return mpld3.fig_to_html(fig)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777)