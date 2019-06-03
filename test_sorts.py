#!/usr/bin/env python
from  __future__ import  print_function,division
from copy import copy
import unittest

from sorting import bubble_sort
from sorting import selection_sort
from sorting import merge_sort
from sorting import quicksort
from sorting import tree_sort
from sorting import heapsort

# from random import shuffle
# A1 = range(10)
# shuffle(A1)
# A2 = range(-10,10)
# shuffle(A2)
A0 = [2,1]
A1 = [2, 7, 5, 8, 9, 4, 3, 6, 0, 1]
A2 = [-1, 3, 4, -4, -5, -7, 0, 1, -8, -6,
      8, 5, -3, -10, 2, 6, 9, 7, -9, -2]

class SortTest(unittest.TestCase):

    def test_bubble(self):
        S0 = bubble_sort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = bubble_sort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = bubble_sort(copy(A2))
        self.assertEqual(S2,sorted(A2))

    def test_selection(self):
        S0 = selection_sort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = selection_sort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = selection_sort(copy(A2))
        self.assertEqual(S2,sorted(A2))

    def test_merge(self):
        trivial = [0]
        Strivial = merge_sort(trivial)
        self.assertEqual(Strivial,trivial)
        S0 = merge_sort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = merge_sort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = merge_sort(copy(A2))
        self.assertEqual(S2,sorted(A2))

    def test_quick(self):
        trivial = [0]
        Strivial = quicksort(trivial)
        self.assertEqual(Strivial,trivial)
        S0 = quicksort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = quicksort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = quicksort(copy(A2))
        self.assertEqual(S2,sorted(A2))

    def test_tree(self):
        S0 = tree_sort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = tree_sort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = tree_sort(copy(A2))
        self.assertEqual(S2,sorted(A2))

    def test_heap(self):
        S0 = heapsort(copy(A0))
        self.assertEqual(S0,sorted(A0))
        S1 = heapsort(copy(A1))
        self.assertEqual(S1,sorted(A1))
        S2 = heapsort(copy(A2))
        self.assertEqual(S2,sorted(A2))

if __name__ == "__main__":
    unittest.main()
