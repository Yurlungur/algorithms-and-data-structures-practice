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
        self.assertEqual(t._children[Direction.LEFT]._data,
                         'lp')
        self.assertEqual(t._children[Direction.LEFT]._children[Direction.LEFT]._data,
                         'left')
        self.assertEqual(t._children[Direction.RIGHT]._data,
                         'right')
        
