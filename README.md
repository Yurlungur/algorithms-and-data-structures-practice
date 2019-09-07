Algorithms and Data Structures Practice
========================================

[![Build Status](https://travis-ci.org/Yurlungur/algorithms-and-data-structures-practice.svg?branch=master)](https://travis-ci.org/Yurlungur/algorithms-and-data-structures-practice)

Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

Just a few example algorithms and data structures with tests. Do not
use these as a real library. They're not optimized for Python and
they're terribly slow! Feel free, however, to use them as reference
implementations for yourself or for educational purposes.

# Install and Run Tests

```bash
git@github.com:Yurlungur/algorithms-and-data-structures-practice.git
cd algorithms-and-data-structures-practice.git
pytest -v
```

# Data structures

### Linked List

- Implemented as doubly linked
- No sentinal node. This would have been a good idea
- Insert and append operations in O(1)
- Delete from beginning and end in (1)
- index in O(N)
- Delete inside list in index time + O(1)
- Better than dynamic array when list size changes regularly but you don't need to index into or search quickly
- Essentially a more feature-rich stack/queue

### Stack

- Defined by two operations: `push` and `pop`
- `push` adds an element to the stack
- `pop` removes the *most* recently added element from the stack and
  returns it
- Last in, first out
- O(1) time for all (two) limited operations
- Applicationsinclude memory management, backtrace, syntax parsing, graph searches

### Queue

- Defined by two operations: `push` and `pop`
- `push` adds an element to t he stack
- `pop` removes the *least* recently added element from the stack and
  returns it
- First in, first  out
- O(1) time for all (two) limited operations
- Applications include: dynamic programming, graph searches

### AATree

- Implementation of Balanced Binary Search Tree
- Resources: [wikipedia](https://en.wikipedia.org/wiki/AA_tree) and [original paper](http://user.it.uu.se/~arnea/abs/simp.html)
- Can be used to implement TreeSort (done) and maintain continually sorted collection
- Insert, search, and delete in O(log(N))
- Construction in O(N log(N))
- Full traversal in O(N)

### Binary Heap

- Resources: [wikipedia](https://en.wikipedia.org/wiki/Binary_heap) and [paper](https://dl.acm.org/citation.cfm?doid=512274.512284)
- Binary tree with two properties:
  - *shape property:* All levels of tree, except deepest one are fully filled. Nodes of last level are filled left to right.
  - *Heap property:* Key stored in each node is greater than or equal to all its children according to some ordering (less than or equal also possible)
- I implement a MaxHeap so root node is largest
- Insertion and deletion are O(log(N))
- Building heap for first time is O(N) and can be done in-place. Done  by "heapifying" bottom of array up.
- Applications include priority Queue and efficient heapsort algorithm. Both implemented.

### Priority Queue

- Defined by two operations `push` and `pop_max`
- Can also check if empty
- Items pushed have a "priority" associated with them. The item with max priority is always popped first.
- Popped items are gone.
- Implemented in multiple ways: AATree and Binary Heap
- Very useful in scheduling (for example threads)
- Can be used for more efficient graph search algorithms such as A*
- Insertion and deletion in O(log(N))
- BST version constructed in O(Nlog(N)) time
- Heap version constructed in O(N) time

### Disjoint Set

- Defined by three operations `add`, `find`, and `union`
    - `add` adds a new set
    - `find` returns representative element of a set
    - `union` merges two sets.
- All operations to disjoint set are, on average, constant time
- Sets are represented as a forest, which I internally compactly implement as a hash table. A more standard implementation would be an array.

# Algorithms

## Sorting Algorithms

### Bubble sort

- The simplest sort O(N^2) time
- Iterates through the array, pairwise exchanging elements
- Largest element will "bubble up" to right of array
- Repeat on subarray not containing largest elements

### Selection Sort

- Walks through array and swaps smallest element to lowest index
- Repeats on subarray
- O(N^2) time
- Easy to perform in-place

### Merge Sort

- If two subarrays are sorted, one can merge them to make the new array sorted
- Merge sort recursively does this on left- and right-halves of array
- O(N log(N)) time. Merge has linear cost. Must be performed log(N) times.

### Quicksort

- Finds "pivot" and ensures  elements smaller than it are to its left
- Recursively performs this on subarrays to left and right of pivot
- Efficient in place
- Worst case: O(N^2) if one partition of array is empty
- Best and average cases: O(N log(N))
- By far fastest sort on average (if there are few repeated elements)

### Heapsort

- Implemented with binary heap
- Essentially selection sort with greatest/least element selected from heap
- O(N log(N)) time. Linear to construct heap. log(N) to acces next
  element from heap. N swaps.

### Treesort
- Implemented by simply inserting elements into self-balancing binary
  search tree then removing them.
- log(N) for each inseart or deletion. N inserts and N deletions. So O(N  log(N)) time.

