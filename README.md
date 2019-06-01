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
