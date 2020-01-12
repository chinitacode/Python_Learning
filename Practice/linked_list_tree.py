class Tree:
        def __init__(self, label, branches=[]):
            self.label = label
            for branch in branches:
                assert isinstance(branch, Tree)
            self.branches = list(branches)
        def __repr__(self):
            if self.branches:
                branch_str = ', ' + repr(self.branches)
            else:
                branch_str = ''
            return 'Tree({0}{1})'.format(repr(self.label), branch_str)
        def is_leaf(self):
            return not self.branches

        def __str__(self):
            return '\n'.join(self.indented())

        def indented(self):
            lines = []
            for b in self.branches:
                for line in b.indented():
                    lines.append('  ' + line)
            return [str(self.label)] + lines

        def is_leaf(self):
            return not self.branches

def fib_tree(n):
    """A Fibonacci tree.

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def leaves(tree):
    """Return the leaf values of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.label]
    else:
        return sum([leaves(b) for b in tree.branches], [])

def height(tree):
    """The height of a tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])

def tree_mutate(tree, f):
    tree.label = f(tree.label)
    for b in tree.branches:
        tree_mutate(b, f)

def prune(t, n):
    """Prune sub-trees whose label value is n.

    >>> t = fib_tree(5)
    >>> prune(t, 1)
    >>> print(t)
    5
      2
      3
        2
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
            
def prune_repeats(t, seen):
    """Remove repeated sub-trees

    >>> def fib_tree(n):
    ...     if n == 0 or n == 1:
    ...         return Tree(n)
    ...     else:
    ...         left = fib_tree(n-2)
    ...         right = fib_tree(n-1)
    ...         return Tree(left.label + right.label, (left, right))
    >>> fib_tree = memo(fib_tree)
    >>> t = fib_tree(6)
    >>> print(t)
    8
      3
        1
          0
          1
        2
          1
          1
            0
            1
      5
        2
          1
          1
            0
            1
        3
          1
            0
            1
          2
            1
            1
              0
              1
    >>> prune_repeats(t, [])
    >>> print(t)
    8
      3
        1
          0
          1
        2
      5
    """
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prune_repeats(b, seen)

### Treating the tree as immutable (as in the ADT)

def tree_map_broken(tree, f):
    """Return a new tree with f applied to all labels"""
    if tree.is_leaf():
        return Tree(f(tree.label))
    else:
        return 1 + max([height(b) for b in tree.branches])

def tree_map(t,f):
    """Return a tree like t but with all labels having f applied to them."""
    return Tree(f(t.label), [tree_map(b,f) for b in t.branches])

### TREES ADT (FROM LECTURE 13)

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree_adt(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree_adt(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree_adt(branch):
            return False
    return True

def is_leaf_adt(tree):
    return not branches(tree)

def print_tree_adt(t, indent=0):
    print('  ' * indent+str(label(t)))
    for b in branches(t):
        print_tree_adt(b, indent + 1)

### FIB_TREE_ADT

def fib_tree_adt(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree_adt(n-2)
        right = fib_tree_adt(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def tree_map_adt(t,f):
    """Return a tree like t but with all labels having f applied to them."""
    return tree(f(label(t)), [tree_map_adt(b,f) for b in branches(t)])

def add10(label):
    return label + 10

### new tree (via ADT) that starts with fib_tree_adt(3) 
### but increases all its labels by 10

print("\ntree ADT")
print_tree_adt(tree_map_adt(fib_tree_adt(3), add10))

### Tree Class immutable

print("\nTree Class immutable")
print(tree_map(fib_tree(3),add10))

### Tree Class mutable

print("\nTree Class mutable")
f3 = fib_tree(3)
tree_mutate(f3, add10)
print(f3)
