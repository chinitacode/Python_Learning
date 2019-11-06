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
