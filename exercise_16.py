#!/usr/bin/env python

import unittest
class CakeThief:

    def get_max_cake_value(self,cake, capacity):
        cake_weight = cake[0]
        cake_value = cake[1]
        max_number_of_bags = capacity / cake_weight
        return max_number_of_bags * cake_value

    def sort_cakes(self,cakes, capacity):
	# need to work on the below for muscle memory
	return sorted(cakes,key=lambda cake: self.get_max_cake_value(cake,capacity), reverse=True)

    def get_max_number_of_bags(self, cake, capacity):
        cake_weight = cake[0]
        cake_value = cake[1]
        max_number_of_bags = capacity / cake_weight
        return max_number_of_bags

    def max_duffel_bag_value(self, cakes, capacity):
	if capacity == 0:
	    return 0
	sorted_cakes = self.sort_cakes(cakes, capacity)
	current_capacity = capacity
	max_duffel_bag_value = 0
	for cake in sorted_cakes:
	    cake_weight = cake[0]
	    cake_value = cake[1]
	    max_bags = self.get_max_number_of_bags(cake, current_capacity)
	    if max_bags < current_capacity:
                max_duffel_bag_value += self.get_max_cake_value(cake, current_capacity)
		current_capacity = current_capacity - ( max_bags * cake_weight)
	return max_duffel_bag_value 

class TestCakeThief(unittest.TestCase):
    def setUp(self):
	self.cake_thief = CakeThief()
	self.cakes = [(7,160), (3,90), (2,15)]
	self.capacity = 20

    def test_get_max_cake_value(self):
	self.assertEquals(self.cake_thief.get_max_cake_value(self.cakes[0], self.capacity), 320)
	self.assertEquals(self.cake_thief.get_max_cake_value(self.cakes[1], self.capacity), 540)
	self.assertEquals(self.cake_thief.get_max_cake_value(self.cakes[2], self.capacity), 150)


    def test_sort_cakes(self):
	sorted_cakes = [(3,90), (7,160), (2,15)]
	self.assertEquals(self.cake_thief.sort_cakes(self.cakes, self.capacity), sorted_cakes)

    def test_max_duffel_bag_value(self):
	self.assertEquals(555, self.cake_thief.max_duffel_bag_value(self.cakes, self.capacity))
	self.assertEquals(0, self.cake_thief.max_duffel_bag_value(self.cakes, 0))
