def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        N=[N[i-1] + N[i] for i in range(len(N))]


def triangles2():
    l = [1]
    while True:
        yield l
        l = [sum(x) for x in zip([0] + l, l + [0])]
        


if __name__ == '__main__':
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    g=triangles()
    for n in range(10):
        print(next(g))
