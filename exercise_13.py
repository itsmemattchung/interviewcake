#!/usr/bin/env python

import unittest

class TestRotationPoint(unittest.TestCase):

    def find_rotation_point(self, words):
        pass


    def setUp(self):
	self.words = [
    	    'ptolemaic',
    	    'retrograde',
    	    'supplant',
    	    'undulate',
    	    'xenoepist',
    	    'asymptote', # <-- rotates here!
    	    'babka',
    	    'banoffee',
    	    'engender',
    	    'karpatka',
    	    'othellolagkage',
    	    ]

    def test_find_rotation_point(self):
        self.assertEquals(self.find_rotation_point(self.words),5)
