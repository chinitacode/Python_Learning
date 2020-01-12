import unittest
from circles import circle_area
from math import pi
'''
test command:
winpty python -m unittest test_circles
or:
winpty python -m unittest # it will search for tests and run them
'''
class TestCircleArea(unittest.TestCase):
    def setUp(self):
        self._f = circle_area

    def test_area(self):
        # Test areas with radius >= 0
        '''
        For the self.assertAlmostEqual method(difference within 10e-7)
        or the self.assertEqual,
        the first argument should be the output of the function
        while the second should be the correct answer
        '''
        r = self._f(1)
        self.assertAlmostEqual(r, pi)
        r = self._f(0)
        self.assertAlmostEqual(r, 0)
        r = self._f(2.1)
        self.assertAlmostEqual(r, pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary(check improper input values)
        '''
        For the self.assertRaises method,
        the first argument should be the type of error that should be raised;
        the second should be the function and
        the third is the argument to the function
        '''
        self.assertRaises(ValueError, self._f, -2)

    def test_types(self):
        # Make sure type errors are raised when the input is not real number
        self.assertRaises(TypeError, self._f, True)
        self.assertRaises(TypeError, self._f, 3+5j)
        self.assertRaises(TypeError, self._f, 'radius')
