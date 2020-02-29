'''
BFS(Depth First Search)广度优先搜索
广度优先搜索是按范围一圈一圈地扩大，就想警察抓小偷，不可能一开始就只奔东边一直深入查找抓犯人。
因为stack这个数据结构先进后出(或后进先出)（LIFO）的性质，我们可以不停地加入新的邻居一直加到最底层；
但对于BFS,我们需要先进先出，先把第一层的邻居搜索完，再搜索第二层的邻居......，所以我们需要队列这个数据结构。
BFS只有迭代这一种实现方式。
E.g. 对于图G：
G={
    'a':{'b','f'},
    'b':{'c','d','f'},
    'c':{'d'},
    'd':{'e','f'},
    'e':{'f'},
    'f':{}
}
BFS先访问a节点的邻接节点b、f；再访问b的邻接节点c、d、f；接下来访问a的另一个邻接节点 f 的邻接节点……
'''
from collections import deque

def BFS(G,s):
    visited = set()
    path = []
    queue = deque()
    queue.append(s)
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            path.append(vertex)
            visited.add(vertex)
            queue += G[vertex]
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

    print(BFS(G, 'a'),'\n')
    print(BFS(G, 'c'),'\n')


# 返回从起点s到达终点d的路径的集合(无环图)
def bfs(G,s,d):
    path = []
    queue = deque()
    queue.append((s,[s]))
    while queue:
        vertex, tmp = queue.popleft()
        if vertex == d:
            path.append(tmp[:])
        if G[vertex]:
            queue += [(nbr, tmp+[nbr]) for nbr in G[vertex]]
    return path

if __name__ == '__main__':
    print(bfs(G, 'a', 'b'), '\n')
    print(bfs(G, 'b', 'f'), '\n')
    print(bfs(G, 'a', 'f'), '\n')
