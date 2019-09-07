#!/usr/bin/env python
from  __future__ import  print_function,division
import unittest
from disjoint_set import DSU

class DisjointSetTest(unittest.TestCase):

    def test_add(self):
        s = DSU()

        s.add('set1')
        s.add('set2')

        self.assertEqual(len(s), 2)

    def test_find(self):
        s = DSU()

        s.add('set1')

        self.assertEqual(s.find('set1'),'set1')

    def  test_union(self):
        s = DSU()

        elements  = ['e11','e12','e21','e22']
        for e in elements:
            s.add(e)

        s.union('e11','e12')
        s.union('e21','e22')
        roots = set([s.find(e) for e in elements])

        self.assertEqual(len(roots),2)
