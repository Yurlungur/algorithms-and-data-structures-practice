# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

from __future__ import print_function, division

class DSU:
    """A disjoint set union data setructure.  Performs set union
    operations in essentially constant time.

    Implemented compactly as a hash table. Could easily instead be
    implemented as an array.

    Implements path compression and union by rank. See:
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self):
        "Initializes a disjoint set union."
        self.parents = {}
        self.rank = {}

    def add(self,x):
        "add x to the set if it doesn't already exist"
        if x not in self.parents:
            self.parents[x] = x
            self.rank[x] = 0

    def find(self,x):
        "find the represent element of set containing x"
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,x,y):
        "merge sets containing x and y"
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            xroot, yroot = yroot,xroot

        self.parents[yroot] = xroot
        if self.rank[xroot] == self.rank[yroot]:
            self.rank[xroot] = self.rank[yroot] + 1

    def __len__(self):
        return len(self.parents)
