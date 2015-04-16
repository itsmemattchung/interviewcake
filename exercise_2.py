#!/usr/bin/env python

from collections import Counter
import unittest

class TempTracker:
    def __init__(self):
        self.temperatures = []

    def insert(self, temperature):
        self.temperatures.append(float(temperature))
        return self.temperatures

    def get_max(self):
        return max(self.temperatures)

    def get_min(self):
        return min(self.temperatures)

    def get_mean(self):
        return sum(self.temperatures) / len(self.temperatures)

    def get_mode(self):
        counter = Counter(self.temperatures)
        return counter.most_common(1)[0][0]
        return counter


class TestTempTracker(unittest.TestCase):

    def setUp(self):
        self.temp_tracker = TempTracker()

    def test_insert(self):
        self.assertEquals(self.temp_tracker.insert(99), [99])
        self.assertEquals(self.temp_tracker.insert(80), [99,80])


    def test_get_max(self):
        self.temp_tracker.temperatures = [0,100,50,99,-55]
        self.assertEquals(self.temp_tracker.get_max(), 100)

    def test_get_min(self):
        self.temp_tracker.temperatures = [0,100,50,99,-55]
        self.assertEquals(self.temp_tracker.get_min(), -55)

    def test_get_mean(self):
        self.temp_tracker.insert(0)
        self.temp_tracker.insert(100)
        self.temp_tracker.insert(50)
        self.temp_tracker.insert(99)
        self.temp_tracker.insert(-55)
        self.assertEquals(self.temp_tracker.get_mean(), 38.8)

    def test_get_mode(self):
        self.temp_tracker.insert(0)
        self.temp_tracker.insert(100)
        self.temp_tracker.insert(50)
        self.temp_tracker.insert(99)
        self.temp_tracker.insert(-55)
        self.temp_tracker.insert(99)
        self.assertEquals(self.temp_tracker.get_mode(), 99.0)

        

