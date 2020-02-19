'''
def binary_search(H):
    start, end = 0, max(H)
    while start < end:
        mid = start + (end - start)//2
        E = mid
        succeed = True
        for h in H:
            if E < h:
                E -= (h-E)
            else:
                E += (E-h)
            if E < 0:
                start = mid + 1
                succeed = False #E值不通过
                break
        if succeed: #如果到最后还剩有能量
            end = mid 
    return end

if __name__ == '__main__':
    N = int(input().strip())
    H = list(map(int,input().strip().split()))
    print(binary_search(H))

'''

def hop(H):
    E = 0
    H.reverse()
    for h in H:
        E = (E + h) >> 1
    return E

if __name__ == '__main__':
    input()
    H = list(map(int,input().strip().split()))
    print(hop(H))
