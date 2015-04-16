#!/usr/bin/env python
# Some notes
# The lowest price has to be BEFORE the highest price
# for every element, need to get difference in price for every subsequent instance
import unittest


class AppleStocks(unittest.TestCase):
    def setUp(self):
        self.stock_prices = []
        self.stock_prices.append(300)
        self.stock_prices.append(325)
        self.stock_prices.append(100)
        self.stock_prices.append(500)
        self.stock_prices.append(400)

    def test_get_max_profit(self):
        self.assertEquals(get_max_profit(self.stock_prices), 400)

