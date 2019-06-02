#!/usr/bin/env python
from  __future__ import  print_function,division
import unittest
from priority_queue import PriorityQueueElement, PriorityQueueTree

priorities = [900,1,2,2,4,5,3]
values =     ["one","two","three","four","five","six","seven"]
psorted,vsorted = zip(*sorted(zip(priorities,values)))
psorted = list(reversed(psorted))
vsorted = list(reversed(vsorted))

class PriorityQueueElementTest(unittest.TestCase):

    def test_init(self):
        e = PriorityQueueElement(1,"one")
        self.assertEqual(len(e),1)
        e.values.push("two")
        self.assertEqual(len(e),2)

    def test_comparison(self):
        a = PriorityQueueElement(1,"one")
        b = PriorityQueueElement(2,"one")
        c = PriorityQueueElement(1,"two")
        d = PriorityQueueElement(0,"two")
        self.assertTrue(a < b)
        self.assertTrue(a == c)
        self.assertTrue(a > d)
        self.assertTrue(a == 1)
        self.assertTrue(a > 0)
        self.assertTrue(a >= 1)
        self.assertTrue(a < 2)
        self.assertTrue(b == 2)
        self.assertTrue(c == 1)
        self.assertTrue(d == 0)

class PriorityQueueTest(unittest.TestCase):

    def test_tree_queue_basic(self):
        q = PriorityQueueTree()
        self.assertTrue(q.is_empty())
        q.insert("one",900)
        self.assertFalse(q.is_empty())
        self.assertTrue(q._T.contains(900))
        q.insert("two",900)
        self.assertTrue(q._T.contains(900))
        q.pop_max()
        self.assertTrue(q._T.contains(900))
        q.pop_max()
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.pop_max())
        self.assertFalse(q._T.contains(900))

    def test_tree_queue_full(self):
        q = PriorityQueueTree(values,priorities)
        for p in priorities:
            self.assertTrue(q._T.contains(p))
        self.assertFalse(q.is_empty())
        for v in vsorted:
            self.assertEqual(q.pop_max(),v)
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.pop_max())

if __name__ == "__main__":
    unittest.main()
