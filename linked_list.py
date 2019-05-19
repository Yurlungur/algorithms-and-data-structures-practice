#!/usr/bin/env python

from __future__ import print_function,division

class Node:
    def __init__(self,
                 data = None,
                 prev_node = None,
                 next_node = None):
        self.data = data
        self._prev = prev_node
        self._next = next_node

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            outstr = "Linked List Node:\n\t[{} {} {}]".format(self.data,
                                                              self._prev,
                                                              self._next)
            return outstr

class DoublyLinkedList:
    "Doubly linked list"
    def __init__(self,*data):
        "Initializes empty linked list"
        self._size = 0
        self._head = None
        self._tail = None
        for d in data:
            self.append(d)

    def get(self,n):
        node = self._find_node(n)
        return node.data

    def set(self,n,val):
        node = self._find_node(n)
        node.data = val

    def insert(self,item,n=0):
        "Inserts element at position n"
        if len(self) == 0 and n in [0,-1]:
            self._add_from_empty(item)
        elif n == -1:
            self.insert(item,len(self)-1)
        elif n == 0:
            self.push(item)
        else:
            node = self._find_node(n)
            prev_node = node._prev
            
            new_node = Node(item,prev_node,node)
            prev_node._next = new_node
            node._prev = new_node
            
            self._size += 1        

    def push(self,item):
        "Add to the beginning of list"
        next_node = self._head
        new_node = Node(item,None,next_node)
        self._head = new_node
        next_node._prev = new_node
        self._size += 1

    def append(self,item):
        "Add to end of list"
        if len(self) == 0:
            self._add_from_empty(item)
        else:
            last_node = self._tail
            new_node = Node(item,last_node,None)
            last_node._next = new_node
            self._tail = new_node
            self._size += 1

    def pop(self,n=0):
        "Deletes element at position n and returns it"
        if n > len(self) - 1 or (n < 0 and abs(n) > len(self)):
            raise ValueError("Can only delete node in list")
        if n < 0:
            return self.pop(len(self) + n)
        if n == 0:
            return self.pop_first()
        if n == len(self) - 1:
            return self.pop_last()
        node = self._find_node(n)
        out  = node.data
        prev_node  = node._prev
        next_node = node._next
        prev_node._next = next_node
        next_node._prev = prev_node
        self._size -= 1
        return out

    def pop_first(self):
        "Deletes first element and returns it"
        if len(self) == 0:
            raise ValueError("List is empty")
        out = self._head.data
        if len(self) == 1:
            self._delete_last()
        else:
            new_head = self._head._next
            self._head = new_head
            new_head._prev = None
            self._size -=1
        return out

    def pop_last(self):
        "Deletes last element and returns it"
        if len(self) == 0:
            raise ValueError("List is empty")
        out = self._tail.data
        if len(self) == 1:
            self._delete_last()
        else:
            new_tail = self._tail._prev
            self._tail = new_tail
            new_tail._next  = None
            self._size -= 1
        return out
            
    def _add_from_empty(self,item):
        "Adds first element"
        self._head = Node(item,None,None)
        self._tail = self._head
        self._size += 1

    def _delete_last(self):
        # garbage collector deals with rest
        self._head = None
        self._tail = None
        self._size -= 1

    def _find_node(self,n):
        "Gets node n from start"
        if n > len(self) - 1 or (n < 0 and abs(n) > len(self)):
            raise ValueError("Can only find node in list. "
                             +"n = {}, len = {}".format(n,len(self)))
        if n < 0:
            new_n = len(self) + n
            return self._find_node(new_n)
        if n == len(self) - 1:
            return self._tail
        node = self._head
        for i in range(n):
            node = node._next
        return node

    def __getitem__(self, index):
        return self.get(index)

    def  __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current._next

    def __len__(self):
        return self._size

    def __repr__(self):
        return "Doubly Linked list of length {}:\n\t{}".format(len(self),self)

    def  __str__(self):
        return str(list(self))
