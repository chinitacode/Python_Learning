def ruler(n):
    assert n >= 0
    if n == 1:
        return '1'
    #shrink the time complecity:
    t = ruler(n-1)
    return t + ' ' + str(n) + ' ' + t



