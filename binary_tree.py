# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from __future__ import print_function,division
from enum import IntEnum

class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1

class BinaryTreeNode:
    def __init__(self,
                 data = None,
                 parent = None,
                 left_child = None,
                 right_child = None):
        self._data = data
        self._parent = parent
        self._children = [left_child,right_child]
        
    def insert(self,data,direction):
        new_node = BinaryTreeNode(data)
        self._insert_node(node,direction)

    def delete_child(self,direction):
        child = self._children[direction]
        can_delete = child.can_delete()
        if not can_delete:
            return False
        new_child = child.child()
        if new_child is not None:
            new_child._parent = self
        self._children[direction] = new_child

    def num_children(self):
        return sum([c is not None for c in self._children])

    def can_delete(self):
        return self.num_children() < 2

    def child(self,direction=None):
        if direction is not  None:
            return self._children[direction]
        for c in self_children:
            if c is not None:
                return c
        return None

    def _insert_node(self,node,direction):
        # Assumes child always exists. Can be sentinel node.
        current_child = self._children[direction]
        node._children[direction] = current_child
        node._parent = self
        self._children[direction] = node

    def __len__(self):
        return self.num_children()

    def __str__(self):
        return str(self._data)

    def  __repr__(self):
        outstr = ("Binary Tree Node:\n"
                  +"Data        = {}\n".format(self)
                  +"Parent      = {}\n".format(self._parent)
                  +"Left child  = {}\n".format(self._children[Direction.LEFT])
                  +"Right child = {}\n".format(self._children[Direction.RIGHT])
        )
        return outstr
    
