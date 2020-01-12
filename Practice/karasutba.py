'''
[Time]: T(n) = 3T(n/2) + O(n/2 + 1) = 3T(n/2) + O(n) = O(nlog2(3)), log2(3)约为1.59
3个size为n/2的recursive call，和recursive call外的padding with 0 and some other additions is linear with the input size。
'''
def karatsuba(x,y):
    n = len(str(x))
    if n == 1:
        return x*y
    half = n//2
    a,b = x//(10**half), x%(10**half)
    c,d = y//(10**half),y%(10**half)
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b, c+d) - ac -bd
    return (10**n)*ac + (10**half)*ad_plus_bc + bd

def karatsuba2(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n // 2

		a = x // 10**(nby2)
		b = x % 10**(nby2)
		c = y // 10**(nby2)
		d = y % 10**(nby2)

		ac = karatsuba2(a,c)
		bd = karatsuba2(b,d)
		ad_plus_bc = karatsuba2(a+b,c+d) - ac - bd

        	# this little trick, writing n as 2*nby2
        	#takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
