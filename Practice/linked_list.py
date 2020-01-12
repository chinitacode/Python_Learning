class Link(object):
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(repr(self.first))
        return 'Link({}, {})'.format(repr(self.first),
                                      repr(self.rest))
def validate(lst):
    return lst is Link.empty or lst.rest is Link.empty or isinstance(lst.rest,Link)

def count_iter(r,value):
    n = 0
    while r is not Link.empty:
        if r.first == value:
            n += 1
        r = r.rest
    return n

def count(r,value):
    if r is Link.empty:
        return 0
    elif r.first == value:
        return 1 + count(r.rest,value)
    else:
        return count(r.rest,value)
    
def extend_link(s1,s2):
    if s2 is Link.empty:
        return
    elif len(s1) == 1:
        s1.rest = Link(s2.first,s2.rest)
    else:
        extend_link(s1.rest,s2)

def extend_link_iter(s1,s2):
    if s2 is Link.empty:
        return
    while s1.rest is not Link.empty:
        s1 = s1.rest
    s1.rest = Link(s2.first,s2.rest)

def deep_map(fn,lst):
    if lst is Link.empty:
        return
    if not isinstance(lst.first,Link):
        lst.first = fn(lst.first)
    else:
        deep_map(fn,lst.first)
    deep_map(fn,lst.rest)

def map_link(f, s):
        if s is Link.empty:
            return s
        else:
            return Link(f(s.first), map_link(f, s.rest))

def join_link(s, separator):
        if s is Link.empty:
            return ""
        elif s.rest is Link.empty:
            return str(s.first)
        else:
            return str(s.first) + separator + join_link(s.rest, separator)

def partitions(n, m):
        """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
        """
        if n == 0:
            return Link(Link.empty) # A list containing the empty partition
        elif n < 0 or m == 0:
            return Link.empty
        else:
            using_m = partitions(n-m, m)
            with_m = map_link(lambda s: Link(m, s), using_m)
            without_m = partitions(n, m-1)
            return with_m + without_m

def print_partitions(n, m):
        lists = partitions(n, m)
        strings = map_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))
