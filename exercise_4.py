#!/usr/bin/env python
import unittest

def highest_product(array_of_ints):
    return reduce(lambda x,y: x * y, get_top_n_numbers(3,sorted(array_of_ints)))

def sort_array_of_ints(array_of_ints):
    return sorted(array_of_ints)

def get_top_n_numbers(n, array_of_ints):
    return array_of_ints[-n:]

class TestHighestProduct(unittest.TestCase):
    def test_highest_product(self):
        test_numbers = [1,8,5,9,7]
        test_numbers2 = [-10,-10,1,3,2]
        self.assertEqual(highest_product(test_numbers), 504)
        self.assertEqual(highest_product(test_numbers2), 300)

    def test_sorted_array_of_ints(self):
        test_numbers = [1,8,5,9,7]
        self.assertEqual([1,5,7,8,9],sort_array_of_ints(test_numbers))
    
    def test_get_top_n_numbers(self):
        test_numbers = [1,5,7,8,9]
        self.assertEqual([7,8,9],get_top_n_numbers(3, test_numbers))

if __name__ == "__main__":
    array_of_ints = [6,25,1,5,7,8,9]
    print "Array of ints: " + ",".join(str(elem) for elem in array_of_ints)
    print "Product: {highest_product}".format(highest_product=highest_product(array_of_ints))
