'''
1.从顶点s开始遍历整个图
2.返回从起点s到达终点d的路径的集合
3.leetcode 797 [所有可能的路径]

[dfs之时间复杂度]：
因为有visited存储已遍历过的顶点，所以在遍历图时，对图中每个顶点至多调用一次dfs函数。
因此遍历图的过程实质上是对每个顶点查找其邻接点的过程，其耗费的时间则取决于所采用的的存储结构。
当用二维数组表示邻接矩阵作图的存储结构时，查找每个顶点的邻接点所需时间为O(N^2),其中N为图中
顶点数。而当以邻接表作图的存储结构时，找邻接点所需时间为O(e),其中e为无向图中边的数或者有向图中弧的数。
由此，当以邻接表作存储结构时，dfs遍历图的时间复杂度为O(N+e)。

1.从顶点s开始遍历整个图
[Method 1]: Recursion
'''
def DFS(G,s,visited = set(), path = []):
    path.append(s)
    visited.add(s)
    for nxt in G[s]:
        if nxt not in visited:
            # print(visited,path)
            DFS(G,nxt,visited, path)
    return path



if __name__ == '__main__':
    G={
        'a':{'b','f'},
        'b':{'c','d','f'},
        'c':{'d'},
        'd':{'e','f'},
        'e':{'f'},
        'f':{}
    }

    visited = set()
    path = []

    '''
    [注意]：小心DFS的参数的闭包！多次调用DFS的话传参一定要传不一样的visited和path!
    例如：
    print(DFS(G,'b'))
    print(DFS(G,'a'))
    会输出：
    ['b', 'd', 'e', 'f', 'c']
    ['b', 'd', 'e', 'f', 'c', 'a']
    因为调用第一个DFS调用后在内存中保存了visited为('b', 'd', 'e', 'f', 'c'),
    所以第二次调用DFS(G,'a')的时候只有'a'没被遍历过。

    所以在测试的时候必须传入新的visited和path！
    '''
    print(DFS(G,'b'))   # ['b', 'f', 'c', 'd', 'e']
    print(DFS(G,'a',visited,path))  # ['a', 'f', 'b', 'c', 'd', 'e']


'''
[Method 2]: Iteration
'''
def DFS_iter(G,s,visited = set(), path = []):
    stack = [s]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
        stack += G[vertex]
    return path

if __name__ == '__main__':
    print(DFS_iter(G,'b'))   # ['b', 'f', 'd', 'e', 'c']
    print(DFS_iter(G,'a',visited,path))  # ['a', 'f', 'b', 'c', 'd', 'e']



'''
2.返回从起点s到达终点d的路径的集合(无环图)

[Method 1]: Recursion
'''
def dfs(G,s,d):
    path = []
    def helper(tmp, start):
        if start == d:
            path.append(tmp[:])
            return
        for vertex in G[start]:
            tmp.append(vertex)
            helper(tmp, vertex)
            tmp.pop()
    helper([s], s)
    return path

if __name__ == '__main__':
    print('\n'+'searching all possible paths: \n')
    print(dfs(G,'a','b')) # [['a', 'b']]
    print('\n'+'searching all possible paths: \n')
    print(dfs(G,'b','f')) # [['b', 'd', 'e', 'f'], ['b', 'd', 'f'], ['b', 'f'],
                          # ['b', 'c', 'd', 'e', 'f'], ['b', 'c', 'd', 'f']]
    print('\n'+'searching all possible paths: \n')
    print(dfs(G,'a','f')) # [['a', 'f'], ['a', 'b', 'd', 'e', 'f'],
                          # ['a', 'b', 'd', 'f'], ['a', 'b', 'f'],
                          # ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'f']]
    print('\n'+'searching all possible paths: \n')
    print(dfs(G,'f','e')) # []


'''
[Method 2]: Iteration

'''
def dfsIter(G,s,d):
    path = []
    stack = [(s, [s])]
    while stack:
        vertex, tmp = stack.pop()
        if vertex == d:
            path.append(tmp[:])
        if G[vertex]:
            stack += [(nbr, tmp+[nbr]) for nbr in G[vertex]]
    return path

if __name__ == '__main__':
    print('\n'+'Calling dfsIter: \n')
    print(dfsIter(G,'a','b')) # [['a', 'b']]
    print('\n'+'searching all possible paths: \n')
    print(dfsIter(G,'b','f')) # [['b', 'd', 'e', 'f'], ['b', 'd', 'f'], ['b', 'f'],
                          # ['b', 'c', 'd', 'e', 'f'], ['b', 'c', 'd', 'f']]
    print('\n'+'searching all possible paths: \n')
    print(dfsIter(G,'a','f')) # [['a', 'f'], ['a', 'b', 'd', 'e', 'f'],
                          # ['a', 'b', 'd', 'f'], ['a', 'b', 'f'],
                          # ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'f']]
    print('\n'+'searching all possible paths: \n')
    print(dfsIter(G,'f','e')) # []
