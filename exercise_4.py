#!/usr/bin/env python
import unittest
import copy

def highest_product(array_of_ints):
    new_array_of_ints = sort_array_of_ints(copy.deepcopy(array_of_ints))
    if is_count_of_top_n_numbers_even(3,new_array_of_ints):
        return reduce(lambda x,y: x * y, get_top_n_numbers(3,(new_array_of_ints)))
    else:
        return reduce(lambda x,y: x * y, get_top_n_numbers(3,remove_first_negative_number((new_array_of_ints))))

def sort_array_of_ints(array_of_ints):
    return sorted(array_of_ints, key=abs)

def get_top_n_numbers(n, array_of_ints):
    return array_of_ints[-n:]

def is_negative(n):
    if n < 0:
        return True
    else:
        return False

def is_count_of_top_n_numbers_even(n, array_of_ints):
    sorted_ints = sort_array_of_ints(array_of_ints)
    top_n_numbers = sorted_ints[-n:]
    counter = 0
    for num in top_n_numbers:
        if num < 0:
            counter += 1
    if counter % 2 == 0:
        return True
    else:
        return False

def remove_first_negative_number(array_of_ints):
    new_array_of_ints = copy.deepcopy(array_of_ints)
    for i, elem in enumerate(new_array_of_ints):
        if is_negative(elem):
            del new_array_of_ints[i]
            break
    return new_array_of_ints

class TestHighestProduct(unittest.TestCase):
    def test_highest_product(self):
        test_numbers = [1,8,5,9,7]
        test_numbers2 = [-10,-10,1,3,2]
        self.assertEqual(highest_product(test_numbers), 504)
        self.assertEqual(highest_product(test_numbers2), 300)

    def test_sorted_array_of_ints(self):
        test_numbers = [1,8,5,9,7]
        test_numbers2 = [2,-300,4,5]
        self.assertEqual([1,5,7,8,9],sort_array_of_ints(test_numbers))
        self.assertEqual([2,4,5,-300], sort_array_of_ints(test_numbers2))
    
    def test_get_top_n_numbers(self):
        test_numbers = [1,5,7,8,9]
        self.assertEqual([7,8,9],get_top_n_numbers(3, test_numbers))

    def test_number_if_negative(self):
        self.assertTrue(is_negative(-1))
        self.assertFalse(is_negative(1))

    def test_count_of_top_3_numbers_is_even(self):
        self.assertTrue(is_count_of_top_n_numbers_even(3,[0,1,2,3,-4,-5]))

    def test_remove_first_negative_number(self):
        test_numbers = [1,2,3,4,5,-6,7]
        test_numbers2 = [1,2,3,4,-5,-6,-7]
        self.assertEqual(remove_first_negative_number(test_numbers), [1,2,3,4,5,7])
        self.assertEqual(remove_first_negative_number(test_numbers2), [1,2,3,4,-6,-7])



if __name__ == "__main__":
    array_of_ints = [6,25,1,5,7,8,9]
    print "Array of ints: " + ",".join(str(elem) for elem in array_of_ints)
    print "Product: {highest_product}".format(highest_product=highest_product(array_of_ints))
