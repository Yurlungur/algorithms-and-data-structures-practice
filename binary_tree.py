# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from __future__ import print_function,division
from enum import IntEnum

class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1

class BinaryTreeNode:
    def __init__(self,
                 data = None,
                 left_child = None,
                 right_child = None):
        self._data = data
        self._children = [left_child,right_child]
        
    def insert(self,data,direction):
        new_node = BinaryTreeNode(data)
        self._insert_node(new_node,direction)

    def delete_child(self,direction):
        child = self._children[direction]
        can_delete = child.can_delete()
        if not can_delete:
            return False
        new_child = child.child()
        self._children[direction] = new_child

    def num_children(self):
        return sum([c is not None for c in self._children])

    def can_delete(self):
        return self.num_children() < 2

    def left(self):
        return self.child(Direction.LEFT)

    def right(self):
        return self.child(Direction.RIGHT)

    def child(self,direction=None):
        if direction is not  None:
            return self._children[direction]
        for c in self._children:
            if c is not None:
                return c
        return None

    def value(self):
        return self._data

    def is_leaf(self):
        return self.num_children() == 0

    def _insert_node(self,node,direction):
        # Assumes child always exists. Can be sentinel node.
        current_child = self._children[direction]
        node._children[direction] = current_child
        self._children[direction] = node

    def __len__(self):
        return self.num_children()

    def __str__(self):
        return str(self._data)

    def  __repr__(self):
        outstr = ("Binary Tree Node:\n"
                  +"Data        = {}\n".format(self)
                  +"Left child  = {}\n".format(self._children[Direction.LEFT])
                  +"Right child = {}\n".format(self._children[Direction.RIGHT])
        )
        return outstr

class AATree:
    """
    Self-balancing binary search tree. Has the following invariants
    1. The level of every leaf node is one.
    2. The level of every left child is exactly one less than that of its parent.
    3. The level of every right child is equal to or one less than that of its parent.
    4. The level of every right grandchild is strictly less than that of its grandparent.
    5. Every node of level greater than one has two children.

    Conceptually: Level tells "depth" at which node lives in tree.
    Horizontal links are not deeper, but simply traverse accross

    Resources:
    https://en.wikipedia.org/wiki/AA_tree
    http://user.it.uu.se/~arnea/abs/simp.html
    """
    def __init__(self):
        self._size = 0
        self._head = None

    def insert_all(self,C):
        "inserts all elements in collection C"
        for val in C:
            self.insert(val)

    def insert(self,key):
        "inserts X into tree."
        if self.contains(key):
            return
        self._head = self._insert_subtree(key,self._head)
        self._size += 1

    def delete(self,key):
        "Deletes key from tree if present"
        if not self.contains(key):
            return
        self._head = self._delete_subtree(key,self._head)
        self._size -= 1

    def contains(self,key):
        "Tests to see if key is in tree"
        if self._head is None:
            return False
        return self._head.contains(key)

    def get_sorted(self):
        "Returns sorted elements of BST"
        out = []
        if self._head is None:
            return out
        self._head.get_sorted(out)
        return out

    def find_min(self):
        "Get min value"
        if self._head is None:
            return None
        return self._head.leftmost().value()

    def find_max(self):
        "Get max value"
        if self._head is None:
            return None
        return self._head.rightmost().value()

    def depth(self,approx=True):
        "Gets depth of tree. Approx algorithm is O(log(N))"
        if self._head is None:
            return 0
        if approx:
            return self._head.approx_depth()
        else:
            return self._head.depth()

    def __len__(self):
        return self._size

    @classmethod
    def _skew(self,T):
        """
        Rebalancing operation.

        Input T is root of subtree to be rebalanced.
        Output is rebalanced subtree.
        """
        #        |
        #   L <- T
        #   /\    \
        #  A  B    R
        # becomes
        #   |
        #   L -> T
        #   /   / \
        #  A   B   R
        if T is None:
            return T
        if T.left() is None:
            return T
        if T.left().level() == T.level():
            # swap pointers of horizontal left links
            L = T.left()
            T._children[Direction.LEFT] = L.right()
            L._children[Direction.RIGHT] = T
            return L
        return T

    @classmethod
    def _split(self,T):
        """
        Rebalancing operation.

        Input T is root of subtree to be rebalanced.
        Output is rebalanced subtree.
        """
        #    |
        #    T -> R -> X
        #   /    /
        #  A    B
        # becomes
        #        |
        #        R
        #       / \
        #      T   X
        #     / \
        #    A   B
        if T is None:
            return T
        if T.right() is None:
            return  T
        if T.right().right() is None:
            return T
        if T.level() == T.right().right().level():
            # We have two horizontal right links.
            # Take middle node, elevate it, and return it.
            R = T.right()
            T._children[Direction.RIGHT] = R.left()
            R._children[Direction.LEFT] = T
            R._level = R._level +  1
            return R
        return T

    @classmethod
    def _insert_subtree(self,X,T):
        """Insert value X into subtree T.
        Returns a pointer to T, now balanced and containing X.
        """
        if T is None:
            # Make a new node to fill T
            # It's level 1
            return AATreeNode(X,1,None,None)
        if X < T.value():
            T._children[Direction.LEFT] = self._insert_subtree(X,T.left())
        elif X > T.value():
            T._children[Direction.RIGHT] = self._insert_subtree(X,T.right())
        else: # If X == T.value() we don't need to insert. No duplicates.
            None
        # Balancing operations.  Will do nothing if skew/split unneeded.
        T = self._skew(T)
        T = self._split(T)
        return T

    @classmethod
    def _delete_subtree(self,X,T):
        """Delete value X from subtree T. (T is a node)
        Returns a pointer to T, now with X deleted.
        """
        if T is None:
            return T
        if X > T.value():
            T._children[Direction.RIGHT] = self._delete_subtree(X,T.right())
        elif X < T.value():
            T._children[Direction.LEFT] = self._delete_subtree(X,T.left())
        else:
            if T.is_leaf():
                return None # let T be garbage collected
            if T.left() is None:
                # swap T with L. Let deleted node be garbage collected.
                L = T._successor()
                T._children[Direction.RIGHT] = self._delete_subtree(L.value(),
                                                                    T.right())
                T._data = L.value()
            else:
                L = T._predecessor()
                T._children[Direction.LEFT] = self._delete_subtree(L.value(),
                                                                   T.left())
                T._data = L.value()
        # Rebalance tree.
        # Decrease level of all nodes on this level if necessary,
        # Then skew and split all nodes  in the new level.
        T._decrease_subtree_level()
        T = self._skew(T)
        T._children[Direction.RIGHT] = self._skew(T.right())
        if T.right() is not None:
            T._children[Direction.RIGHT]._children[Direction.RIGHT] \
                = self._skew(T.right().right())
        T = self._split(T)
        T._children[Direction.RIGHT] = self._split(T.right())
        return T

class AATreeNode(BinaryTreeNode):
    def __init__(self,
                 data = None,
                 level = 1,
                 left_child = None,
                 right_child = None):
        self._level = level
        super().__init__(data,
                         left_child,
                         right_child)

    def level(self):
        return self._level
    
    def contains(self,key):
        "Subtree containing this node contains key?"
        if self._data == key:
            return True
        if key < self._data and self.left() is not None:
            return self.left().contains(key)
        if key > self._data and self.right() is not None:
            return self.right().contains(key)
        return False

    def leftmost(self):
        if self.left() is None:
            return self
        return self.left().leftmost()
    
    def rightmost(self):
        if self.right() is None:
            return self
        return self.right().rightmost()
    
    def approx_depth(self,curr_depth=1):
        "Returns approximate depth of subtree  owned by this node."
        # log(N) runtime
        if self.left() is not None:
            return self.left().approx_depth(curr_depth+1)
        if self.right() is not None:
            return self.right().approx_depth(curr_depth+1)
        return curr_depth
    
    def depth(self,curr_depth=1):
        "Returns depth of subtree owned by this node"
        # O(N) runtime
        if self.left() is not None:
            left_depth = self.left().depth(curr_depth+1)
        else:
            left_depth = curr_depth
        if self.right() is not None:
            right_depth = self.right().depth(curr_depth+1)
        else:
            right_depth = curr_depth
        return max(left_depth,right_depth)

    def get_sorted(self,collection):
        if self.left() is not None:
            self.left().get_sorted(collection)
        collection.append(self._data)
        if self.right() is not None:
            self.right().get_sorted(collection)

    def _predecessor(self):
        "Get node containing key closest to me but smaller"
        if self.left() is None:
            return None
        return self.left().rightmost()

    def _successor(self):
        "Get node containing key closest to me but greater"
        if self.right() is None:
            return None
        return self.right().leftmost()
    
    def _decrease_subtree_level(self):
        "Remove links that skip levels on subtree owned by this node"
        if self.left() is not  None:
            left_level = self.left().level()
        else:
            left_level = 0
        if self.right() is not  None:
            right_level = self.right().level()
        else:
            right_level = 0
        new_level = min(left_level,right_level) + 1
        if new_level < self.level():
            self._level = new_level
            if new_level < self.right().level():
                self.right()._level = new_level
