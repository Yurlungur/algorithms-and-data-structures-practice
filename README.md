Algorithms and Data Structures Practice
========================================

[![Build Status](https://travis-ci.org/Yurlungur/algorithms-and-data-structures-practice.svg?branch=master)](https://travis-ci.org/Yurlungur/algorithms-and-data-structures-practice)

Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

Just a few example algorithms and data structures with tests.

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
