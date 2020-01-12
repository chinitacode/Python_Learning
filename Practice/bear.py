class Bear:
    """A Bear.
    
    
    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear

    >>> print(str_(oski))
    a bear
    >>> print(repr_(oski))
    Bear()
    """

    def __init__(self):
        self.__repr__ = lambda: 'repr oski' # instance attribute
        self.__str__ = lambda: 'str oski the bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__repr__())
    print(oski.__str__())

print_bear()

def repr_(x):
    s = type(x).__repr__(x)
    if not isinstance(s,str):
        raise TypeError
    return s

def str_(x):
    s = type(x).__str__(x)
    if not isinstance(s,str):
        raise TypeError
    return s
