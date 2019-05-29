#!/usr/bin/env python
import unittest
from binary_tree import BinaryTreeNode, Direction

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
            self.assertEqual(child.can_delete(),
                             True)
        self.assertEqual(len(t),2)
        self.assertEqual(t.child(Direction.LEFT)._data,2)
        t.delete_child(Direction.RIGHT)
        self.assertEqual(len(t),1)
        t.delete_child(Direction.LEFT)
        self.assertEqual(len(t),1)
        self.assertEqual(t.child(Direction.LEFT)._data,0)
        t.insert(3,Direction.LEFT)
        t.child(Direction.LEFT).insert(4,Direction.RIGHT)
        self.assertEqual(t.child(Direction.LEFT).can_delete(),
                         False)
        self.assertEqual(t.delete_child(Direction.LEFT),False)
        self.assertEqual(t.child(Direction.LEFT)._data,3)
