# Recursive solution
def gray_code(n):
    if n == 0:
        return [0]
    res = gray_code(n-1)
    return res + [code + (1 << (n-1)) for code in reversed(res)]


# Iterative solution
def grayCode(n):
    size = 1 << n
    res = []
    # Use the conversion formula of Binary to Gray Code:
    # XORing(exclusive or) the binary current index
    # and the 1 bit right shifted(>>) index
    for i in range(size):
        res.append(i ^ (i >> 1))
    return res
