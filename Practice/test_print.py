'''
To test print() after value asignment:
'''
def square(arg):
    print(arg**2)

if __name__ == '__main__':
    res = []
    for i in range(5):
        r = square(i)
        res.append(i)
    print(res)
