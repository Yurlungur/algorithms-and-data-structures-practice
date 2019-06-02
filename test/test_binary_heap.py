#!/usr/bin/env python
import  unittest
from binary_heap import MaxHeap
from copy import  copy

to_add   = [1,-50,900,3,3,4,2,88.5,1e5,-0.1]
to_add_2 = [-2,9,10,-3,-4,-1,100,22,99.3,-0.0,0.0,0,33]

class MaxHeapTest(unittest.TestCase):

    def test_empty(self):
        h = MaxHeap()
        self.assertEqual(len(h),0)
        self.assertEqual(h.capacity(),256)
        self.assertEqual(h.get_array(),[])

    def test_construct(self):        
        h = MaxHeap(elements=to_add,do_copy=True)
        self.assertEqual(h.peek(),max(to_add))

    def test_sort(self):
        s1 = MaxHeap.heapsort(copy(to_add))
        s2 = list(sorted(to_add))
        self.assertEqual(s1,s2)

    def test_insert(self):
        h = MaxHeap()
        for i in range(len(to_add)):
            h.insert(to_add[i])
            self.assertEqual(h.peek(),max(to_add[:i+1]))
            self.assertEqual(len(h),i+1)

    def test_pop(self):
        h = MaxHeap(elements=to_add,do_copy=True)
        self.assertEqual(h.peek(),max(to_add))
        self.assertEqual(len(h),len(to_add))
        for i,v in enumerate(reversed(sorted(to_add))):
            print(i,v)
            self.assertEqual(h.pop(),v)
            self.assertEqual(len(h),len(to_add) - i - 1)
        self.assertEqual(len(h),0)
        self.assertIsNone(h.pop())
        for i in range(len(to_add_2)):
            h.insert(to_add_2[i])
            self.assertEqual(h.peek(),max(to_add_2[:i+1]))
            self.assertEqual(len(h),i+1)

if __name__ == "__main__":
    unittest.main()
