import unittest
from sorting import quick_sort2

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self._f = quick_sort2

    def test_empty(self):
        alist = []
        self._f(alist)
        self.assertEqual([],alist)

    def test_one(self):
        alist = [1]
        self._f(alist)
        self.assertEqual([1],alist)
        alist = [22]
        self._f(alist)
        self.assertEqual([22],alist)

    def test_two(self):
        alist = [1, -2]
        self._f(alist)
        self.assertEqual([-2, 1],alist)
        alist = [5, 8]
        self._f(alist)
        self.assertEqual([5, 8],alist)

    def test_multiple(self):
        alist = [40, 5, 23, 10, 33]
        self._f(alist)
        self.assertEqual([5, 10, 23, 33, 40],alist)
        alist = [4, 3, 5, 1, 2]
        self._f(alist)
        self.assertEqual([1, 2, 3, 4, 5],alist)

    def test_duplicates(self):
        alist = [2, 2, 2]
        self._f(alist)
        self.assertEqual([2, 2, 2],alist)
        alist = [5, 8, 10, 8, 9, 10, 8]
        self._f(alist)
        self.assertEqual([5, 8, 8, 8, 9, 10, 10],alist)
        alist = [12, 8, 10, 8, 9, 10, 8]
        self._f(alist)
        self.assertEqual([8, 8, 8, 9, 10, 10, 12],alist)
