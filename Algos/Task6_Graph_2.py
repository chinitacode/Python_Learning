'''

	连通图
	最短路径
	实现 Dijkstra 算法
	实现拓扑排序

[连通图]
·在无向图中，若从顶点v到顶点w之间存在路径，则两点连通；
·在有向图中，连接顶点v和w的路径中所有边都必须同向；
·如果图中任意两点都是连通的，那么图被称作连通图。

Goal: Partition vertices into connected components
[connected components]
Initialize all vertices v as unmarked.

For each unmarked vertex v,
run DFS to identify all vertices discovered as part of the same component.

'''








'''
[最短路径]
BFS不考虑边缘权重，只考虑边缘数量。
比如在实际应用（地图）中，只考虑站（具体地点，如城市），不考虑距离、速度限制、交通等等。

单源（single source）最短路径问题：
即从一个顶点u出发，
·找出到另一顶点v的最小代价路径。
·求出从u到图中每个顶点的最小代价距离（single-source-multiple-destination）。

[Dijikstra算法]
·贪婪：求全局最优解时每次都从局部最优解出发
·使用优先级队列
·核心是使用了广度优先搜索，只是搜索的顺序用的是贪婪的思想，来解决赋权有向图或者无向图(有权值)的单源最短路径问题
·算法最终得到一个最短路径树

Dijkstra算法采用的是一种贪心的策略，
声明一个数组dis来保存源点到各个顶点的最短距离和一个保存已经找到了最短路径的顶点的集合：
T，初始时，原点 s 的路径权重被赋为 0 （dis[s] = 0）。
若对于顶点 s 存在能直接到达的边（s,m），则把dis[m]设为w（s, m）,
同时把所有其他（s不能直接到达的）顶点的路径长度设为无穷大。
初始时，集合T只有顶点s。
然后，从dis数组选择最小值，则该值就是源点s到该值对应的顶点的最短路径，并且把该点加入到T中，OK，此时完成一个顶点，
然后，我们需要看看新加入的顶点是否可以到达其他顶点并且看看通过该顶点到达其他点的路径长度是否比源点直接到达短，
如果是，那么就替换这些顶点在dis中的值。
然后，又从dis中找出最小值，重复上述动作，直到T中包含了图的所有顶点。

[Pseudocode]
Dijikstra(s,G):
Initialize: MinPriorityQueue(PQ), visited HashSet, parent HashMap, and distances to infinity
Enqueue {s,0} onto the PQ
while PQ is not empty:
    dequeue node curr from front of queue (pop出min heap的top，即到起点s的最短distance)
    if curr is not visited:
        add curr to visited set
        if curr == G: return parent map
        for each of curr's neighbors nbr not in visited set(针对没被访问过得邻点，即BFS):
            if path through curr to nbr is shorter:
                update nbr's distance(即从起始点s到nbr的距离)
                update curr as nbr's parent in parent map
                enqueue {nbr, distance} into PQ
    if we get here, then there's no path (即没有return值)

'''
from AdjListGraph import Graph
from AdjListGraph import Vertex
import heapq

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous: #if v has parent node
        path.append(v.previous.getVertexID())  #最终得到的path是从终点到起点的list，需要手动reverse
        shortest(v.previous, path)
    return

def dijkstra(G, source, destination):
    print('''Dijkstra's shortest path''')
    # Set the distance for the source node to zero
    source.setDistance(0)

    # Put tuple pair into the priority queue, 用distance代表优先级，此处为minheap,top为最小距离
    # 初始化时除了起点source距离刚被设置为0,其他点都是inf
    unvisitedQueue = [(v.getDistance(), v) for v in G]
    heapq.heapify(unvisitedQueue)

    while len(unvisitedQueue): #只要队列不为空
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisitedQueue) #局部最优解(最小距离)
        current = uv[1] #Vertex对象，当前的点
        current.setVisited() #已经确定了最短距离

        # for next in v.adjacent: #查看current的邻居
        for next in current.adjacent:
            # if visited, skip
            if next.visited: #如果next的最短距离已经确定了
                continue
            newDist = current.getDistance() + current.getWeight(next)

            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print('Updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))
            else:
                print('Not updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        # 2. Put all vertices not visited into the queue
        unvisitedQueue = [(v.getDistance(), v) for v in G if not v.visited] #因为距离可能更新
        heapq.heapify(unvisitedQueue)

if __name__ == '__main__':
    G = Graph(True)
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))
            #( a , b,   4)
            #( a , c,   1)
            #( b , e,   4)
            #( c , b,   2)
            #( c , d,   4)
            #( d , e,   4)
    source = G.getVertex('a')
    destination = G.getVertex('e')
    dijkstra(G, source, destination)
    #Dijkstra's shortest path
    #Updated : current = a next = b newDist = 4
    #Updated : current = a next = c newDist = 1
    #Updated : current = c next = b newDist = 3
    #Updated : current = c next = d newDist = 5
    #Updated : current = b next = e newDist = 7
    #Not updated : current = d next = e newDist = 7
    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print ('The shortest path from a to e is: %s' % (path[::-1]))
    #a  to  a --> 0
    #a  to  b --> 3
    #a  to  c --> 1
    #a  to  d --> 5
    #a  to  e --> 7
    #The shortest path from a to e is: ['a', 'c', 'b', 'e']

'''
[简洁应用版，针对邻接列表]：

'''
G_list = {
    'a':{'b':4,'c':1},
    'b':{'e':4},
    'c':{'b':2,'d':4},
    'd':{'e':4},
    'e':{}
}

#一般想寻找给定两点的最短路径，Dijkstra 算法必须传入三个参数，一是图G，一是源点 s，一是终点d。
import heapq
def dijikstra(G,s,d):
    parent = {s:None}
    visited = set()
    distance = {}
    for node in G:
        distance[node] = float('inf')
    distance[s] = 0
    unvisitedQueue = [(distance[node], node) for node in G]
    heapq.heapify(unvisitedQueue)

    while unvisitedQueue:
        curr_dis, curr_node = heapq.heappop(unvisitedQueue)
        visited.add(curr_node)
        for nbr in G[curr_node]:
            if nbr in visited: continue
            newDist = curr_dis + G[curr_node][nbr]
            if newDist < distance[nbr]:
                distance[nbr] = newDist
                parent[nbr] = curr_node
        while unvisitedQueue:
            heapq.heappop(unvisitedQueue) #清空优先级队列
        unvisitedQueue = [(distance[node], node) for node in G if node not in visited]
        heapq.heapify(unvisitedQueue)
    print(distance)
    if distance[d] != float('inf'):
        path = [s,d]
        node = parent[d]
        while node != s:
            path.insert(1,node)
            node = parent[node]
        return distance[d],path
    return float('inf'),[]

if __name__ == '__main__':
    dijikstra(G_list,'c','d')
    #{'c': 0, 'a': inf, 'b': 2, 'd': 4, 'e': 6}
    #(4, ['c', 'd'])


'''
把邻接矩阵转换为邻接列表：
'''
def matrixToList(matrix):
    n = len(matrix)
    res = {node:{} for node in range(n)}
    for node in range(n):
        for nbr in range(n):
            if matrix[node][nbr] != 0:
                res[node][nbr] = matrix[node][nbr]
    return res

if __name__ == '__main__':
    graph_list = [
      [0,30,15,0,0,0],
      [5,0,0,0,20,30],
      [0,10,0,0,0,15],
      [0,0,0,0,0,0],
      [0,0,0,10,0,0],
      [0,0,0,30,10,0]
      ]
    print(matrixToList(graph_list))
    '''
    {0: {1: 30, 2: 15},
     1: {0: 5, 4: 20, 5: 30},
     2: {1: 10, 5: 15},
     3: {},
     4: {3: 10},
     5: {3: 30, 4: 10}}
    '''
    dijikstra(matrixToList(graph_list),0,5)
    '''
    {0: 0, 1: 25, 2: 15, 3: 50, 4: 40, 5: 30}
    (30, [0, 2, 5])
    '''

'''
[Bellman Ford算法]
贝尔曼-福特算法(Bellman–Ford algorithm )用于计算出起点到各个节点的最短距离，支持存在负权重的情况
-它的原理是对图进行最多V-1次松弛操作，得到所有可能的最短路径。
其优于迪科斯彻算法的方面是边的权值可以为负数、实现简单，缺点是时间复杂度过高，高达O(VE)。但算法可以进行若干种优化，提高了效率。

-Bellman Ford算法每次对所有的边进行松弛，每次松弛都会得到一条最短路径，所以总共需要要做的松弛操作是V - 1次。
在完成这么多次松弛后如果还是可以松弛的话，那么就意味着，其中包含负环。

-相比狄克斯特拉算法(Dijkstra algorithm),其最大优点便是Bellman–Ford支持存在负权重的情况，并且代码实现相对简单。
缺点便是时间复杂度较高，达到O(V*E)，V代表顶点数，E代表边数。

可用于解决以下问题：
1.从A出发是否存在到达各个节点的路径(有计算出值当然就可以到达)；
2.从A出发到达各个节点最短路径(时间最少、或者路径最少等)
3.图中是否存在负环路（权重之和为负数）

其思路为：
1.初始化时将起点s到各个顶点v的距离dist(s->v)赋值为∞，dist(s->s)赋值为0
2.后续进行最多n-1次遍历操作(n为顶点个数,上标的v输入法打不出来...),对所有的边进行松弛操作,假设:
  所谓的松弛，以边ab为例，若dist(a)代表起点s到达a点所需要花费的总数，
  dist(b)代表起点s到达b点所需要花费的总数,weight(ab)代表边ab的权重，
  若存在:
    (dist(a) +weight(ab)) < dist(b)
  则说明存在到b的更短的路径,s->...->a->b,更新b点的总花费为(dist(a) +weight(ab))，父节点为a
3.遍历都结束后，若再进行一次遍历，还能得到s到某些节点更短的路径的话，则说明存在负环路

思路上与狄克斯特拉算法(Dijkstra algorithm)最大的不同是每次都是从源点s重新出发进行"松弛"更新操作，
而Dijkstra则是从源点出发向外扩逐个处理相邻的节点，不会去重复处理节点，这边也可以看出Dijkstra效率相对更高点。
 Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of Fibonacci heap).
 Dijkstra doesn’t work for Graphs with negative weight edges, Bellman-Ford works for such graphs.
 Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems.
 But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.
'''
def bellman_ford(graph, source):
    dist = {}
    p = {}
    max = 10000
    for v in graph:
        dist[v] = max  #赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0

    for i in range(len( graph ) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u    #完成松弛操作，p为前驱节点

    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None, None  #判断是否存在环路

    return dist, p

def test():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }
    dist, p = bellman_ford(graph, 'a')
    print(dist)
    print(p)

#有负循环的时候(When there's a negative circle)
def testfail():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':-2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }
    dist, p = bellman_ford(graph, 'a')
    print(dist)
    print(p)

if __name__ == '__main__':
    test()
    #{'a': 0, 'b': -1, 'c': 2, 'd': -2, 'e': 1}
    #{'a': None, 'b': 'a', 'c': 'b', 'd': 'e', 'e': 'b'}
    testfail()
    #None
    #None


'''
[***小结***]
1.广度优先算法BFS主要适用于无权重向图重搜索出源点到终点的步骤最少的路径，当方向图存在权重时，不再适用
2.狄克斯特拉算法Dijkstra主要用于有权重的方向图中搜索出最短路径，但不适合于有负权重的情况.
因为Dijkstra's algorithm这样假设：对于处理过的节点，没有前往该节点的更短路径。
这种假设仅在没有负权边时才成立。因此，不能将Dijkstra's algorithm用于包含负权边的图。
3.贝尔曼-福特算法Bellman–Ford主要用于存在负权重的方向图中(没有负权重也可以用，但是效率比Dijkstra低很多)，搜索出源点到各个节点的最短路径
4.Bellman–Ford可以判断出图是否存在负环路，但存在负环路的情况下不支持计算出各个节点的最短路径。
只需要在结束(节点数目-1)次遍历后，再执行一次遍历，若还可以更新数据则说明存在负环路

'''





'''
[拓扑]：
所谓“拓扑”就是把实体抽象成与其大小、形状无关的“点”，而把连接实体的线路抽象成“线”，
进而以图的形式来表示这些点与线之间关系的方法，其目的在于研究这些点、线之间的相连关系。
表示点和线之间关系的图被称为拓扑结构图。拓扑结构与几何结构属于两个不同的数学概念。

在几何结构中，我们要考察的是点、线之间的位置关系，或者说几何结构强调的是点与线所构成的形状及大小。
如梯形、正方形、平行四边形及圆都属于不同的几何结构，但从拓扑结构的角度去看，
由于点、线间的连接关系相同，从而具有相同的拓扑结构即环型结构。
也就是说，不同的几何结构可能具有相同的拓扑结构。

[拓扑排序]：
在将一件事情分解为若干个小事情时，会发现小事情之间有完成的先后次序之分，
若不按照特定的顺序完成，则会使得整件事情无法完成。
因此这需要获取工作安排表。而拓扑排则怎能根据小事情之间的先后次序生成这样一个工作安排表（拓扑序列）。
但请注意，能满足要求的拓扑序列不止一个。

几乎在所有的项目，甚至日常生活，待完成的不同任务之间通常都会存在着某些依赖关系，
这些依赖关系会为它们的执行顺序行程表部分约束。

对于这种依赖关系，很容易将其表示成一个有向无环图（Directed Acyclic Graph，DAG，无环是一个重要条件），
并将寻找其中依赖顺序的过程称为拓扑排序（topological sorting）。

很多情况下，拓扑排序问题往往会出现在一些中等复杂程度的计算系统中。
这方面最典型的例子莫过于软件安装了，
现在大多数操作系统都至少会有一个自动安装软件组件的系统（Ubuntu Linux 系统中的 apt-get，
CentOS Linux 系统中的 RPM，Mac OS X 系统中的 brew 等），
这些系统会自动检测依赖关系中缺少的部分，并下载安装它们，对于这一类工作，相关组件就必须按照一定的拓扑顺序来安装。

DAG 分析
（1）拓扑排序并不唯一
（2）不含回路的有向图（有向无环图）——一定存在拓扑排序。

在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序：
·每个顶点出现且只出现一次；
·若A在序列中排在B的前面，则在图中不存在从B到A的路径。

[Iteration]：
其实就是找每个节点的入度(indegree)，将入度为0的节点(只有从此节点出发的路径)作为起点，
并且同时将其neighbors的入度减1，如果为0则继续加入stack。
如果剩下入度非0的顶点（输出的顶点数小于图中的顶点数），就说明有回路，不存在拓扑排序。
'''
def topoSort(G):
    #初始化入度字典
    indegrees = dict((u,0) for u in G.keys())
    #完成每个节点的入度计算
    for u in G:
        for nbr in G[u]:
            indegrees[nbr] += 1
    #maintain stack，把入度为0的节点入栈
    stack = [u for u in indegrees if indegrees[u] == 0]
    #初始化拓扑序列
    seq = []
    while stack:
        curr = stack.pop()
        seq.append(curr)
        for nbr in G[curr]:
            indegrees[nbr] -= 1
            #把入度为0的节点入栈
            if indegrees[nbr] == 0:
                stack.append(nbr)
    if len(seq) != len(G): return None
    return seq

if __name__ == '__main__':
    print(topoSort(G))
    #['a', 'b', 'c', 'd', 'e', 'f']


'''
[Recursion]:
'''
def naiveTopoSort(G,V=None):
    #需要排序的顶点的set集合
    if V is None:
        V = set(G.keys())
    if len(V) == 1:
        return list(V)
    #当前节点
    curr = V.pop()
    #seq为剩余顶点的拓扑序列
    seq = naiveTopoSort(G,V)
    #记录当前节点curr应该插入拓扑序列的index
    minIdx = 0
    for i,v in enumerate(seq):
        if curr in G[v]: #如果有从v到curr的路径，则curr排在v后面
            minIdx = i+1
    seq.insert(minIdx,curr)
    return seq

if __name__ == '__main__':
    naiveTopoSort(G)
    #['a', 'b', 'c', 'd', 'e', 'f']
