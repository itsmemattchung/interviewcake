#!/usr/bin/env python

import unittest

def condense_meeting_ranges(meeting_ranges):
    pass

def sort_meetings(meeting_ranges):
    pass


class MergingRanges(unittest.TestCase):
    def test_condense_meeting_ranges(self):
        meeting_ranges = [(0,1), (3,5), (4,8), (10,12), (9,10)]
        condensed_ranges = [(0,1), (3,8), (9,12)]
        self.assertEquals(condense_meeting_ranges(meeting_ranges), condense_meeting_ranges)

    def test_sort_meetings(self):
        meeting_ranges = [(3,5), (0,1),(4,8), (10,12), (9,10)]
        sorted_meeting_ranges = [(0,1), (3,5), (4,8), (10,12), (9,10)]
        self.assertEquals(sort_meetings(meeting_ranges), sorted_meeting_ranges) 
