def approx_eq(x,y,tolerance = 1e-4):
    return abs(x-y) < tolerance


def pi():
    pi = 0
    prev = 999
    i = 1
    sign = 1
    while not approx_eq(prev,pi):
        prev = pi
        pi = pi + sign*(1/i) 
        sign = sign*(-1)
        i += 2
    return 4*pi
