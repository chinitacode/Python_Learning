from math import pi
'''
docstring testing command:
winpty python -m doctest circles.py
* -m means 'module'
'''

def circle_area(r):
    '''
    >>> circle_area(0)
    0.0
    >>> circle_area(1)
    pi
    '''

    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (r**2)

'''
# Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"] # j is the square root of -1
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius = r, area = A))
'''
