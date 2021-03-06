#!/usr/bin/env python
from  __future__ import  print_function,division
import unittest
from binary_tree import BinaryTreeNode, AATree, Direction
import math

class BinaryTreeNodeTest(unittest.TestCase):

    def test_insert(self):
        t = BinaryTreeNode()
        t._data = 'root'
        self.assertEqual(len(t),0)
        t.insert('left',Direction.LEFT)
        self.assertEqual(len(t),1)
        t.insert('right',Direction.RIGHT)
        self.assertEqual(len(t),2)
        t.insert('lp',Direction.LEFT)
        self.assertEqual(t.child(Direction.LEFT)._data,
                         'lp')
        self.assertEqual(t.child(Direction.LEFT).child(Direction.LEFT)._data,
                         'left')
        self.assertEqual(t.child(Direction.RIGHT)._data,
                         'right')

    def test_delete(self):
        t = BinaryTreeNode()
        t._data = 'root'
        t.insert(0,Direction.LEFT)
        t.insert(1,Direction.RIGHT)
        t.insert(2,Direction.LEFT)
        for child in t._children:
            self.assertTrue(child.can_delete())
        self.assertEqual(len(t),2)
        self.assertEqual(t.child(Direction.LEFT)._data,2)
        t.delete_child(Direction.RIGHT)
        self.assertEqual(len(t),1)
        t.delete_child(Direction.LEFT)
        self.assertEqual(len(t),1)
        self.assertEqual(t.child(Direction.LEFT)._data,0)
        t.insert(3,Direction.LEFT)
        t.child(Direction.LEFT).insert(4,Direction.RIGHT)
        self.assertFalse(t.child(Direction.LEFT).can_delete())
        self.assertFalse(t.delete_child(Direction.LEFT))
        self.assertEqual(t.child(Direction.LEFT)._data,3)

class AATreeTest(unittest.TestCase):

    def test_init(self):
        T = AATree()
        self.assertEqual(len(T),0)
        self.assertEqual(T.depth(),0)
        self.assertFalse(T.contains(792.5))
        self.assertIsNone(T.find_min())
        self.assertIsNone(T.find_max())

    def test_insert(self):
        T = AATree()
        to_insert = [999,-4.0,-5.0,3,2,5,1e4]
        first_insert = 0
        imax = max(to_insert + [first_insert])
        imin = min(to_insert + [first_insert])
        idepth = math.ceil(math.log2(len(to_insert))+1)
        T.insert(first_insert)
        T.insert(first_insert) # checks duplicates
        self.assertEqual(len(T),1)
        self.assertIsNotNone(T._head)
        self.assertTrue(T.contains(first_insert))
        self.assertEqual(T.depth(),1)
        for i,val in enumerate(to_insert):
            T.insert(val)
            self.assertEqual(len(T),i+1+1)
            self.assertTrue(T.contains(val))
        self.assertEqual(T.depth(False),idepth)
        self.assertEqual(T.find_min(),imin)
        self.assertEqual(T.find_max(),imax)

    def test_contains(self):
        to_insert = [900,1,2,2,4,5,3]
        T = AATree()
        for i in to_insert:
            T.insert(i)
            self.assertTrue(T.contains(i))

    def test_tsort(self):
        T = AATree()
        to_insert = [999,-4.0,-5.0,3,2,5,1e4,0]
        T.insert_all(to_insert)
        Tsort = T.get_sorted()
        self.assertEqual(Tsort,sorted(to_insert))

    def test_level_order(self):
        T = AATree()
        to_insert = [1,2,3]
        T.insert_all(to_insert)
        level_order = T.traverse_level_order()
        self.assertEqual(level_order,[2,1,3])
        T = AATree()
        to_insert = [-3,-2,-1,0,1,2,3]
        T.insert_all(to_insert)
        level_order = T.traverse_level_order()
        Tsort = T.get_sorted()
        self.assertEqual(Tsort,to_insert)
        self.assertEqual(level_order,[0,-2,2,-3,-1,1,3])

    def test_delete(self):
        T = AATree()
        to_insert = list(range(64))
        to_delete = list(to_insert[::2]) + [to_insert[-1]]
        remaining = sorted(set(to_insert) - set(to_delete))
        T.insert_all(to_insert)
        T.delete(1e11) # tests it won't delete things that don't exist
        self.assertEqual(len(T),len(to_insert))
        self.assertEqual(T.depth(),math.log2(len(to_insert)))
        for i,v in enumerate(to_delete):
            T.delete(v)
            self.assertFalse(T.contains(v))
            self.assertEqual(len(T),len(to_insert)-(i+1))
        self.assertEqual(T.depth(False),math.ceil(math.log2(len(T))))
        self.assertEqual(T.find_min(),remaining[0])
        self.assertEqual(T.find_max(),remaining[-1])
        self.assertEqual(T.get_sorted(),remaining)
        T.delete(T.find_max())
        self.assertEqual(T.find_max(),remaining[-2])

if __name__ == "__main__":
    unittest.main()
