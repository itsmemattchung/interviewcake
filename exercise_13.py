#!/usr/bin/env python

import unittest

class TestRotationPoint(unittest.TestCase):

    def find_rotation_point(self, words):
	# aaabcd
	# aaabbc
	# find first letter between `a`, and `b` that is different
	# the first letter that is different. if `b` is greater, than skip to next item
	# if `b` at the index is less than, that is the rotation point
	char_of_words = [ list(word) for word in words ]
	for i, item in enumerate(char_of_words[:-1]):
	        for letter_index, letter in enumerate(char_of_words[i]):
			if letter < char_of_words[i+1][letter_index]:
			    break
	    		else:
			    return i + 1
            


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
