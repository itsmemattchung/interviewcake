#!/usr/bin/env python

import unittest 
import operator

def get_product_for_array(array):
    return reduce(operator.mul, array, 1)

def get_products_of_all_ints_except_at_index(array):
    products = []
    for index, element in enumerate(array):
        new_array = list(array)
        #Remove element at index
        del new_array[index]
        products.append(get_product_for_array(new_array))

    return products


        

class TestHighestProductExceptIndex(unittest.TestCase):
    def setUp(self):
        self.array_of_ints = [1,7,3,4]

    def test_get_product_for_array(self):
        self.assertEquals(get_product_for_array([1,2,3,4]),24)

    def test_get_products_of_all_ints_except_at_index(self):
        self.assertEquals(get_products_of_all_ints_except_at_index(self.array_of_ints), [84,12,28,21])
