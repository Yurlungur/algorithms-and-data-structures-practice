# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

# Implementation of a few simple sorting algorithms. Dirt slow because
# this is Python.

from __future__ import print_function,division
import math
from copy import copy
from binary_tree import AATree
from binary_heap import MaxHeap

def bubble_sort(A):
    "Bubble sorts array A O(N^2)"
    for i in range(len(A)-1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
    return A

def selection_sort(A):
    "Sorts array A by selection O(N^2)"
    for i in range(len(A)):
        j,Amin = find_min(A,i)
        swap(A,i,j)
    return A

def merge_sort(A):
    "Sorts A recursively by merge sort"
    if len(A) < 3:
        return  bubble_sort(A)
    B = copy(A)
    midpoint = len(A) // 2
    Aleft = merge_sort(A[:midpoint])
    Aright = merge_sort(A[midpoint:])
    i = 0
    j = 0
    for k in range(len(B)):
        if i < len(Aleft) and j < len(Aright):
            if Aleft[i]  < Aright[j]:
                B[k] = Aleft[i]
                i += 1
            else:
                B[k] = Aright[j]
                j += 1
        elif i < len(Aleft):
            B[k] = Aleft[i]
            i += 1
        elif j < len(Aright):
            B[k] = Aright[j]
            j += 1
        else:
            raise ValueError("i and j both out of bounds")
    return B

def tree_sort(A):
    "Sorts with TreeSort"
    T = AATree()
    T.insert_all(A)
    return T.get_sorted()

def heapsort(A):
    "Sorts with heapsort"
    return MaxHeap.heapsort(A)

def quicksort(A,lo = None, hi = None):
    "Sorts A with quicksort"
    if len(A) < 3:
        return bubble_sort(A)
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(A) - 1
    if lo < hi:
        p = qs_partition_lomuto(A,lo,hi)
        quicksort(A,lo,p-1)
        quicksort(A,p+1,hi)
    return A

def qs_partition_lomuto(A,lo,hi):
    "Sets pivot to element at max index. walks through array with one index."
    # median of 3 pivoting
    mid = lo + (hi-lo)//2  # avoids overflow
    if A[mid] < A[lo]:
        swap(A,lo,mid)
    if A[hi] < A[lo]:
        swap(A,lo,hi)
    if A[mid] < A[hi]:
        swap(A,mid,hi)
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        if A[j] < pivot:
            swap(A,i,j)
            i += 1
    swap(A,i,hi)
    return i

def qs_partition_hoare(A,lo,hi):
    "Sets pivot to element at midpoint. Walks through array with two indices."
    pivot = qs_get_pivot(A,lo,hi) # A[lo + (hi - lo) // 2]
    while True:
        i = lo - 1
        j = hi + 1
        while True:
            i = i + 1
            if A[i] >= pivot:
                break
        while True:
            j = j - 1
            if A[j] <= pivot:
                break
        if i >= j:
            return j
        swap(A,i,j)

def qs_get_pivot(A,lo,hi):
    possibles = bubble_sort([A[lo],A[lo + (hi-lo)//2],A[hi]])
    return possibles[1] # median

def find_min(A,istart):
    """Finds minimum element and minimum index in array A,
    starting at istart
    """
    Amin = math.inf
    for i in range(istart,len(A)):
        if A[i] <  Amin:
            Amin = A[i]
            imin = i
    return imin,Amin

def swap(A,i,j):
    "swaps elements at indices i and j in A"
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
