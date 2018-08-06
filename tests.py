import stockPrices
import pytest
import unittest
import pandas as pd
import numpy as np
import datetime


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        stockPrices.app.testing = True
        self.app = stockPrices.app.test_client()


    def test_index(self):
        # tester = self.app.test_client(self)
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b'Hello, World!')




    def test_filterData(self):


        randomArray = np.arange(0,10)

        randomIndex = ['7/2/2011', '8/6/2012', '11/13/2013', '5/26/2011', '5/2/2001']
        randomIndex = [datetime.datetime.strptime(x, '%m/%d/%Y') for x in randomIndex]

        openDict = pd.concat([pd.DataFrame({'Open': randomArray}), pd.DataFrame({'values': randomIndex})], axis=1)
        openDict.set_index('values')
        value = openDict['Open']
        response = stockPrices.filterData(openDict,'2001', '2013')
        flag = 'Open' == response.name
        self.assertEqual(flag,True)

    def test_movingAverage(self):
        inputArray = np.arange(10,22)
        array = [0.0,10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.5]

        response = stockPrices.calculateMovingAverages((inputArray))
        flag = True
        for i in range(len(response)):
            movingAverage = float(response[i].split("<br/>")[0].split(":")[1])
            if movingAverage != array[i]:
                flag = False
        self.assertEqual(flag, True)








if __name__ == '__main__':
    unittest.main()