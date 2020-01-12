# Ratio numbers
from math import gcd

class Ratio:
    """A mutable ratio.

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> f + 1
    Ratio(8, 5)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """

    def __init__(self,n,d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({}, {})'.format(self.numer,self.denom)

    def __str__(self):
        return '{}/{}'.format(self.numer,self.denom)

    def __add__(self,other):
        if isinstance(other,Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom

        elif isinstance(other,int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other

        g = gcd(n,d)
        r = Ratio(n // g, d // g)
        return r

    __radd__ =__add__

    def __float__(self):
        return self.numer / self.denom

print(Ratio(1,3)+Ratio(6,6))
print(1+Ratio(1,3))
print(Ratio(1,3)+1.0)
print(Ratio(1,3)+1.4)
