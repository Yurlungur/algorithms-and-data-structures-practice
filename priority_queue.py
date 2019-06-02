# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from  __future__ import  print_function,division
from functools import total_ordering
from binary_tree import AATree
from linked_list import Queue

@total_ordering
class PriorityQueueElement:
    def __init__(self,key,value):
        self.key = key
        self.values = Queue()
        self.values.push(value)

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
