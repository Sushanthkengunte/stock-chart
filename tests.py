import stockPrices
import unittest
import pandas as pd
import numpy as np
import datetime
import Model

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        stockPrices.app.testing = True
        self.app = stockPrices.app.test_client()


    def test_index(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)




    def test_filterData(self):
        randomArray = np.arange(0,10)
        randomIndex = ['7/2/2011', '8/6/2012', '11/13/2013', '5/26/2011', '5/2/2001', '5/2/2002', '5/2/2003',
                       '5/2/2004', '5/2/2005', '5/2/2006']
        randomIndex = [datetime.datetime.strptime(x, '%m/%d/%Y') for x in randomIndex]
        openDict = pd.DataFrame({'Open': randomArray}, index=randomIndex)
        rangeOf = openDict.loc['2001':'2013'].values
        response = Model.filterData(openDict,'2001', '2013').values
        flag = True
        if len(rangeOf) != len(response):
            flag = False

        if flag:
            for i in range(len(rangeOf)):
                if rangeOf[i] != response[i]:
                    flag = False

        self.assertEqual(flag,True)



    def test_movingAverage(self):
        inputArray = np.arange(10,22)
        array = [0.0,10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.5]

        response = Model.calcMovingAvg(inputArray,10)
        flag = True
        for i in range(len(response)):
            # movingAverage = float(response[i].split("<br/>")[0].split(":")[1])
            if response[i] != array[i]:
                flag = False
        self.assertEqual(flag, True)



if __name__ == '__main__':
    unittest.main()