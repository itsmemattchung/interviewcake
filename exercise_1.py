#!/usr/bin/env python
# Some notes
# The lowest price has to be BEFORE the highest price
# for every element, need to get difference in price for every subsequent instance
import unittest


# results[profit] = (buy_index, sell_index)
def get_max_profit(stock_prices):
    profits = {}
    for buy_index, purchase_price in enumerate(stock_prices):
        future_stocks = stock_prices[buy_index:]
        for sell_index, sell_price in enumerate(future_stocks, start=buy_index):
            profits[sell_price - purchase_price] = (buy_index, sell_index)
    return profits


class AppleStocks(unittest.TestCase):
    def setUp(self):
        self.stock_prices = []
        self.stock_prices.append(300)
        self.stock_prices.append(325)
        self.stock_prices.append(100)
        self.stock_prices.append(500)
        self.stock_prices.append(400)

    def test_get_max_profit(self):
        self.assertEquals(get_max_profit(self.stock_prices)[400], (2,3) )

