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

[BFS的复杂度分析]  

BFS是一种借用队列来存储的过程，分层查找，优先考虑距离出发点近的点。
无论是在邻接表还是邻接矩阵中存储，都需要借助一个辅助队列，v个顶点均需入队，最坏的情况下，空间复杂度为O（v）。

邻接表形式存储时，每个顶点均需搜索一次，时间复杂度T1=O（v），从一个顶点开始搜索时，开始搜索，
访问未被访问过的节点。最坏的情况下，每个顶点至少访问一次，每条边至少访问1次，这是因为在搜索的过程中，
若某结点向下搜索时，其子结点都访问过了，这时候就会回退，故时间复 杂度为O(E)，算法总的时间复 度为O(|V|+|E|)。

邻接矩阵存储方式时，查找每个顶点的邻接点所需时间为O(V)，即该节点所在的该行该列。
又有V个顶点，故算总的时间复杂度为O(|V|^2)。

BFS的时间复杂度和DFS一样，只是一个是横向搜索一个是纵向搜索。
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
