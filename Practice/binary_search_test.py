import unittest
from binary_search import binarysearch2

class TestBinarySearch1(unittest.TestCase):
    def setUp(self):
        self._f = binarysearch2

    def test_empty(self):
        alist = []
        r = self._f(alist, 5)
        self.assertEqual(-1, r)

    def test_one(self):
        alist = [1]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)

    def test_two(self):
        alist = [1,10]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 2)
        self.assertEqual(-1, r)
        r = self._f(alist, 10)
        self.assertEqual(1, r)
        r = self._f(alist, 11)
        self.assertEqual(-1, r)

    def test_multiple(self):
        alist = [1,2,3,4,5]
        r = self._f(alist, 5)
        self.assertEqual(4, r)
        r = self._f(alist, 4)
        self.assertEqual(3, r)
        r = self._f(alist, 2)
        self.assertEqual(1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 6)
        self.assertEqual(-1, r)
        r = self._f(alist, 0)
        self.assertEqual(-1, r)

    def test_duplicate(self):
        alist = [1,1,1,2,3,3,3,3,3,3,4,5,5,5]
        r = self._f(alist, 5)
        self.assertEqual(5, alist[r])
        r = self._f(alist, 4)
        self.assertEqual(4, alist[r])
        r = self._f(alist, 2)
        self.assertEqual(2, alist[r])
        r = self._f(alist, 3)
        self.assertEqual(3, alist[r])
        r = self._f(alist, 1)
        self.assertEqual(1, alist[r])
        r = self._f(alist, 6)
        self.assertEqual(-1, -1)
        r = self._f(alist, 0)
        self.assertEqual(-1, -1)
    '''
    def test_first_index(self):
        alist = [1,1,1,2,3,3,3,3,3,3,4,5,5,5]
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 3)
        self.assertEqual(4, r)
    '''
    def test_last_index(self):
        alist = [1,1,1,2,3,3,3,3,3,3,4,5,5,5]
        r = self._f(alist, 1)
        self.assertEqual(2, r)
        r = self._f(alist, 4)
        self.assertEqual(alist[r - 1], 3)
