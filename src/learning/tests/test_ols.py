import logging as log
import pandas as pd
import numpy as np
import numpy.testing as npt
import sys
import unittest
import learning.ols as ols

log.basicConfig(stream=sys.stdout, level=log.DEBUG,
                format='%(asctime)-15s %(threadName)s %(filename)s %(levelname)s %(message)s')


class TestOLS(unittest.TestCase):

    def testLearning(self):
        ldf = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [
                           20, 30, 10, 40, 50], "C": [32, 234, 23, 23, 42523]})

        model = ols.Ols()
        model.learn(y=ldf['C'], x=ldf[['A', 'B']])

    def testPredict(self):
        ldf = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [
                           20, 30, 10, 40, 50], "C": [32, 234, 23, 23, 42523]})
        pdf = pd.DataFrame(
            {"A": [10, 20, 30, 40, 50], "B": [20, 30, 10, 40, 50]})

        model = ols.Ols()
        model.learn(y=ldf['C'], x=ldf[['A', 'B']])

        result = model.predict(pdf)

        expected = np.array(
            [-6375.333333, 3610.666667, -1492.333333, 18553., 28539.])
        npt.assert_allclose(result, expected)