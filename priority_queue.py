# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from  __future__ import  print_function,division
from functools import total_ordering
from binary_tree import AATree
from linked_list import Queue
from binary_heap import MaxHeap

@total_ordering
class PriorityQueueElement:
    def __init__(self,key,value):
        self.key = key
        self.values = Queue()
        self.values.push(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values.peek()

    def __len__(self):
        return len(self.values)

    def  __eq__(self,other):
        if hasattr(other,"key"):
            return self.key == other.key
        else:
            return self.key == other

    def __lt__(self,other):
        if hasattr(other,"key"):
            return self.key < other.key
        else:
            return self.key < other

class PriorityQueueTree:
    "Implementation of priority Queue as tree"
    def __init__(self,
                 vals=None,
                 priorities=None):
        self._T = AATree()
        if priorities is not None and vals is not None:
            if len(priorities) != len(vals):
                raise ValueError("Must be as many priorities as values.")
            for v,p in zip(vals,priorities):
                self.insert(v,p)

    def is_empty(self):
        return len(self) < 1

    def insert(self,value,priority):
        element = self._T.get(priority)
        if element is not None:
            element.values.push(value)
        else:
            element = PriorityQueueElement(priority,value)
            self._T.insert(element)

    def pop_max(self):
        if self.is_empty():
            return None
        element = self._T.find_max()
        if element is None:
            return element
        if len(element.values) > 1:
            return element.values.pop()
        key = element.key
        out = element.values.peek()
        self._T.delete(element)
        return out

    def __len__(self):
        return len(self._T)

class PriorityQueueHeap:
    "Implementation of a priority queue as a heap"
    # Reuse of elements used in tree implementation is inefficient
    # because we don't need  a linked list. Oh well.
    def __init__(self,
                 vals=None,
                 priorities=None):
        if priorities is not None and vals is not None:
            if len(priorities) != len(vals):
                raise ValueError("Must be as many priorities as values.")
            elements = [PriorityQueueElement(p,v) for v,p in zip(vals,priorities)]
        else:
            elements = None
        self._h = MaxHeap(elements=elements)

    def insert(self,value,priority):
        element = PriorityQueueElement(priority,value)
        self._h.insert(element)

    def pop_max(self):
        element = self._h.pop()
        if element is None:
            return element
        return element.pop()

    def peek(self):
        element = self._h.peek()
        if element is None:
            return element
        return element.peek()

    def is_empty(self):
        return len(self) < 1

    def shrink_to_size(self):
        "Shrinks heap capacity to current size"
        self._h.shrink_to_size()

    def __len__(self):
        return len(self._h)
