#!/usr/bin/env python
import  unittest
from linked_list import Node,DoublyLinkedList,Stack,Queue

class DoublyLinkedListTest(unittest.TestCase):

    def test_node(self):
        node = Node(1.0)
        self.assertEqual(node.data,1.0)
        self.assertIsNone(node._prev)
        self.assertIsNone(node._next)

    def test_empty_init(self):
        l = DoublyLinkedList()
        self.assertEqual(len(l),0)

    def test_insert_get(self):
        l = DoublyLinkedList()
        l.insert("two")
        l.insert(1.0)
        l.insert(0)
        self.assertEqual(len(l),3)
        self.assertEqual(l._head.data,0)
        self.assertEqual(l._head._next.data,1.0)
        self.assertEqual(l._head._next._next.data,"two")
        self.assertEqual(l._head._next._next,l._tail)
        self.assertEqual(l._head._next,l._tail._prev)
        self.assertIsNone(l._head._prev)
        self.assertIsNone(l._tail._next)
        self.assertEqual(l.get(0),0)
        self.assertEqual(l.get(1),1.0)
        self.assertEqual(l.get(2),"two")
        self.assertEqual(l.get(-1),"two")
        self.assertEqual(l.get(-3),0)
        bad = False
        try:
            l.get(4)
        except ValueError:
            bad = True
        self.assertTrue(bad)
        bad = False
        try:
            l.get(-4)
        except ValueError:
            bad = True
        self.assertTrue(bad)

    def test_append_get(self):
        l = DoublyLinkedList(0,-1.0)
        self.assertEqual(len(l),2)
        self.assertEqual(l.get(0),0)
        self.assertEqual(l.get(1),-1.0)
        self.assertEqual(l._head.data,0)
        self.assertEqual(l._tail.data,-1.0)
        self.assertEqual(l._head._next,l._tail)
        self.assertEqual(l._tail._prev,l._head)
        self.assertIsNone(l._head._prev)
        self.assertIsNone(l._tail._next)

    def test_pop(self):
        l = DoublyLinkedList(0,1,2,3,4)
        self.assertEqual(l.pop(),0)
        self.assertEqual(l.pop(1),2)
        self.assertEqual(len(l),3)
        self.assertEqual(l.pop(-1),4)
        for i in range(len(l)):
            l.pop()
        self.assertEqual(len(l),0)

    def test_iter(self):
        to_iterate = list(range(10))
        l = DoublyLinkedList(*to_iterate)
        for i,j in zip(to_iterate,l):
            self.assertTrue(i == j)

class StackTest(unittest.TestCase):

    def test_init(self):
        stack  = Stack()
        self.assertEqual(len(stack),0)

    def test_push(self):
        stack = Stack()
        to_push = 33
        stack.push(to_push)
        self.assertEqual(len(stack),1)
        self.assertEqual(stack.peek(),to_push)
        to_push = "thirty three"
        stack.push(to_push)
        self.assertEqual(len(stack),2)
        self.assertEqual(stack.peek(),to_push)

    def test_pop(self):
        stack =  Stack()
        to_push = [-5.0,0,"five",True]
        for item in to_push:
            stack.push(item)
        self.assertEqual(len(stack),len(to_push))
        for i in range(len(to_push)):
            self.assertEqual(stack.pop(),to_push[len(to_push)-1-i])
        self.assertEqual(len(stack),0)

class QueueTest(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(len(queue),0)

    def test_push(self):
        queue = Queue()
        to_push = [33, 0.0, "thirty three"]
        for item in to_push:
            queue.push(item)
        self.assertEqual(len(queue),len(to_push))
        self.assertEqual(queue.peek(),to_push[0])

    def test_pop(self):
        queue =  Queue()
        to_push = [-5,0.0,"five",True,[],[1]]
        for item in to_push:
            queue.push(item)
        for item in to_push:
            self.assertEqual(queue.pop(),item)
        self.assertEqual(len(queue),0)

if __name__ == "__main__":
    unittest.main()
