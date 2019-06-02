# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from __future__ import print_function, division
from copy import copy

class MaxHeap:
    """A maximum binary heap
    implemented as an "Array" (actaully a Python list)
    """

    def  __init__(self,
                  elements=None,
                  initial_capacity=256,
                  do_copy=False):
        """Constructor. Build from elements. Or,
        if elements not provided. Creates new heap with initial_capacity.
        Elements can be copied if do_copy set to true.
        """
        if elements is not None:
            if do_copy:
                elements = list(copy(elements))
            else:
                assert type(elements) is list
            self._size = len(elements)
            self._A = elements
            start_ind = len(self) #self._parent_ind(len(self._A)) + 
            for i in reversed(range(self._root_ind(),start_ind)):
                self._max_heapify(i)
        else:
            self._size = 0
            self._A = [None for i in range(initial_capacity)]

    def peek(self):
        "See root element of heap"
        return self._A[self._root_ind()]

    def pop(self):
        "Removes root of heap and returns it"
        if len(self) < 1:
            return None
        root = self._root_ind()
        end = len(self) - 1
        val = self._A[root]
        self._swap(root,end)
        self._size -= 1
        self._max_heapify(root)
        return val

    def insert(self,data):
        "Inserts data into the heap"
        new_len = len(self) + 1
        ind = len(self)
        if new_len > self.capacity():
            self._A.append(data)
        else:
            self._A[ind] = data
        self._size = new_len
        while ind > self._root_ind():
            parent = self._parent_ind(ind)
            if self._A[ind] <= self._A[parent]:
                return # we're done. everything is well-ordered
            self._swap(ind,parent)
            ind = parent

    def get_array(self, do_copy=False):
        "Expose copy of internal array"
        if do_copy:
            return copy(self._A[:self._size])
        else:
            return self._A[:self._size]

    def get_sorted(self):
        "Performs heapsort. Is destructive."
        end = len(self) - 1
        while end > self._root_ind():
            self._swap(end,0)
            self._sift_down(self._root_ind(),end)
            end -= 1
        return self._A

    def capacity(self):
        "How big is the internal array?"
        return len(self._A)

    def shrink_to_size(self):
        "Shrinks capacity to size"
        if self.capacity() > len(self):
            self._A = self._A[:len(self)]

    @classmethod
    def heapsort(cls,A):
        "Sorts array A in-place with a heap sort"
        h = MaxHeap(elements=A,do_copy=False)
        return h.get_sorted()

    def __len__(self):
        return self._size
    
    def _max_heapify(self, i: int):
        "Enforces that subarray self._A[i:] satisfies the heap property"
        left = self._left_ind(i)
        right = self._right_ind(i)
        largest = i
        if left < len(self) and self._A[left] > self._A[largest]:
            largest = left
        if right < len(self) and self._A[right] > self._A[largest]:
            largest = right
        if largest != i:
            self._swap(i,largest)
            self._max_heapify(largest)

    def _sift_down(self,
                   start=None,
                   end=None):
        if start is None:
            start = self._root_ind()
        if end is None:
            end = len(self)
        root = start
        while self._left_ind(root) < end:
            left = self._left_ind(root)
            right = self._right_ind(root)
            swap = root
            if left < end and self._A[swap] < self._A[left]:
                swap = left
            if right < end and self._A[swap] < self._A[right]:
                swap = right
            if swap == root:
                return
            self._swap(root,swap)
            root = swap

    def _swap(self, i: int, j: int):
        "Swaps elements at indices i and j"
        temp = self._A[i]
        self._A[i] = self._A[j]
        self._A[j] = temp

    @classmethod
    def _root_ind(self) -> int:
        "Root index"
        return 0

    @classmethod
    def _parent_ind(self, i: int) -> int:
        "Parent of element at index i"
        return (i - 1) // 2

    @classmethod
    def _left_ind(self, i: int) -> int:
        "Left child of element at index i"
        return 2*i + 1

    @classmethod
    def _right_ind(self, i: int) -> int:
        "Right child of element at index i"
        return 2*i + 2
