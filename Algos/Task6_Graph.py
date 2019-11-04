'''
【图】
	实现有向图、无向图、有权图、无权图的邻接矩阵和邻接表表示方法
	实现图的深度优先搜索、广度优先搜索
	实现 Dijkstra 算法
	实现拓扑排序

【对应的 LeetCode 练习题】
	Number of Islands（岛屿的个数）
	英文版：https://leetcode.com/problems/number-of-islands/description/
	中文版：https://leetcode-cn.com/problems/number-of-islands/description/
	Valid Sudoku（有效的数独）
	英文版：https://leetcode.com/problems/valid-sudoku/
	中文版：https://leetcode-cn.com/problems/valid-sudoku/

ADT Graph:
     Graph(self)               #图的创建
     is_empty(self)            #空图判断
     vertex_num(self)          #返回顶点个数
     edge_num(self)            #返回边的个数
     vertices(self)            #获得图中顶点的集合
     edges(self)               #获得图中边的集合
     add_vertex(self,vertex)   #增加一个顶点
     add_edge(self,v1,v2)      #在v1，v2间加边
     get_edge(self,v1,v2)      #获得边的有关信息
     out_edges(self,v)         #获得v的所有出边
     degree(self,v)            #检查v的度

图是二维上的平面结构，并不是我们之前学的那些简单的线性结构，所以它的高效简洁表示存在一定困难，
这里介绍两种有效的方式：

1.[邻接矩阵 Adjacency Matrix]：
邻接矩阵是图的最基本表示方法，它是表示图中顶点间邻接关系的方阵，对于n个顶点的图G=（V，E），
其邻接矩阵是一个 n x n 方阵，图中每个顶点（按顺序）对应矩阵里的一行一列，矩阵元素表示图中的邻接关系
Aij = w( i , j ) 如果两顶点之间有边，w(i,j)为该边的权
Aij = 0 或 inf 如果两顶点之间无边
————————————————
Maintain a two-dimensional V-by-V boolean array;
for each edge v-w in graph: adj[v][w] = adj[w][v] = True
无向图的邻接矩阵都是对称矩阵，其邻接矩阵关于全为0的对角线对称。
[缺点]：图的邻接矩阵经常是比较稀疏的，当采用邻接矩阵表示这种图时，空间浪费会非常大。
'''
class Vertex:
    def __init__(self, node):
        self.id = node
        # Mark all nodes unvisited
        self.visited = False

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def getVertexID(self):
        return self.id

    def setVertexID(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)

class Graph:
    #Construct a 10-by-10 undirected graph
    def __init__(self, numVertices=10, directed=False):
        self.adjMatrix = [[None] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices #容量
        self.vertices = [] #list => dictionary: {id:vertex},使得getVertex更快；
        self.directed = directed
        for i in range(0, numVertices):
            newVertex = Vertex(i)  #把每个点当成一个vertex对象
            self.vertices.append(newVertex)

    def addVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices: #假设此图不支持拓展
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n): #n为id，e.g。城市名，如北京
        for vertxin in range(0, self.numVertices): #需要在list里按index一个个查找
            if n == self.vertices[vertxin].getVertexID(): #比对id
                return vertxin
        return None

    #E.G.加一条航线
    def addEdge(self, frm, to, cost=0):
        #print("from",frm, self.getVertex(frm))
        #print("to",to, self.getVertex(to))
        if self.getVertex(frm) is not None and self.getVertex(to) is not None:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            #如果是无向图，则需要添加对称关系
            if not self.directed:
                # For directed graph do not add this
                self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        #出于安全考虑，为了避免其他人改变内部数据结构，只能返回备份
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(str(self.adjMatrix[u][v]) if self.adjMatrix[u][v] is not None else '/')
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] is not None:
                    vid = self.vertices[v].getVertexID()
                    wid = self.vertices[u].getVertexID()
                    edges.append((wid, vid, self.adjMatrix[u][v]))
        return edges

    def getNeighbors(self, n):
        neighbors = []
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                for neighbor in range(0, self.numVertices):
                    if (self.adjMatrix[vertxin][neighbor] is not None):
                        neighbors.append(self.vertices[neighbor].getVertexID())
        return neighbors

    def isConnected(self, u, v):
        uidx = self.getVertex(u)
        vidx = self.getVertex(v)
        return self.adjMatrix[uidx][vidx] is not None

    def get2Hops(self, u):
        neighbors = self.getNeighbors(u)
        print(neighbors)
        hopset = set()
        for v in neighbors:
            hops = self.getNeighbors(v)
            hopset |= set(hops)
        return list(hopset)

if __name__ == '__main__':
    graph = Graph(6,True)
    graph.addVertex(0, 'a')
    graph.addVertex(1, 'b')
    graph.addVertex(2, 'c')
    graph.addVertex(3, 'd')
    graph.addVertex(4, 'e')
    graph.addVertex(5, 'f')
    graph.addVertex(6, 'g') #Doing nothing
    graph.addVertex(7, 'h') #Doing nothing

    print('Vertices: ', graph.getVertices())
    print('Before adding edges: Matrix: ', graph.printMatrix())

    graph.addEdge('a','b',1)
    graph.addEdge('a','c',2)
    graph.addEdge('b','d',3)
    graph.addEdge('b','e',4)
    graph.addEdge('c','d',5)
    graph.addEdge('c','e',6)
    graph.addEdge('d','e',7)
    graph.addEdge('e','a',8)
    print('After adding edges, Matrix: ', graph.printMatrix())
    print('Edges: ', graph.getEdges())
    print('Neighbors of a: ',graph.getNeighbors('a') )
    print('Is a connected to e? ', graph.isConnected('a','e'))
    print('2hops of a: ', graph.get2Hops('a'))
    print('\n')

'''
#Or:
首先给出一个使用邻接矩阵建立的图类，输入参数为图的邻接矩阵，
同时，还会有一个unconn参数用以设定无关联情况的特殊值，默认值为0
'''
inf = float('inf')  #定义一个无穷大的量表示无边情况


#采用邻接矩阵实现
class Graph:
    def __init__(self,mat,unconn = 0):   #初始化
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for 'Graph'.")
        self._mat = [mat[i][:] for i in range(vnum)]      #使用拷贝的数据
        self._unonn = unconn
        self._vnum = vnum

    def vertex_num(self):      #返回结点数目
        return self._vnum

    def _invalid(self,v):      #检验输入的结点是否合法
        return v < 0 or v >= self._vnum

    def add_adge(self,vi,vj,val=1):   #增加边
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + 'is not a valid vertex.')
        self._mat[vi][vj] = val

    def get_adge(self,vi,vj):   #得到边的信息
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + 'is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edges(self,vi):    #得到vi出发的所有边
        if self._invalid(vi):
            raise GraphError(str(vi)+' is not a valid vertex.')
        return self._out_edges(self._mat[vi],self._unconn)

    @staticmethod
    def _out_edges(row,unconn): #辅助函数
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges

    def __str__(self):          #输出的str方法
        return '[\n' + ',\n'.join(map(str,self._mat)) + '\n]' + '\nUnconnected: ' + str(self._unconn)

'''
2.[邻接表]：
为了降低图表示的空间代价，人们提出了很多邻接矩阵的压缩版表示方法，邻接表就是其中的一种。
所谓邻接表，就是为图中每个顶点关联一个边表，就构成了图的一种表示，给出示例如下：
'''
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        #set distance to infinity for all nodes
        self.distance = float('inf')
        #mark all nodes unvisited
        self.visited = False
        #Predecessor
        self.previous = None

    #weight 为node与neighbor节点之间的cost，e.g.distance
    def addNeighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    #return a list
    def getConnections(self): # neighbor keys
        return self.adjacent.keys()

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __lt__(self, other):
        return self.distance < other.distance and self.id < other.id


class Graph:
    def __init__(self, directed = False):
        # key is string, vertex id
        # value is Vertex
        self.vertDictionary = {}
        self.numVertices = 0
        self.directed = directed

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def isDirected(self):
        return self.directed

    def vertexCount(self):
        return self.numVertices

    def addVertex(self, node):
        self.numVertices += 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, node):
        if n in self.vertDictionary:
            return self.vertDictionary[node]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        if not self.directed:
            self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getEdges(self):
        edges = []
        for key, currentVert in self.vertDictionary.items():
            for nbr in currentVert.getConnections():
                currentVertID = currentVert.getVertexID()
                nbrID = nbr.getVertexID()
                edges.append((currentVertID, nbrID, currentVert.getWeight(nbr))) #tuple
        return edges

    def getNeighbors(self, node):
        vertex = self.vertDictionary[node]
        return vertex.getConnections()


if __name__ == '__main__':
    #construct a directed graph
    G = Graph(True)
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a','b',1)
    G.addEdge('a','c',1)
    G.addEdge('b','d',1)
    G.addEdge('b','e',1)
    G.addEdge('c','d',1)
    G.addEdge('c','e',1)
    G.addEdge('d','e',1)
    G.addEdge('e','a',1)
    print('Edges: \n', G.getEdges())
    for k in G.getEdges():
        print(k)
    for k in G.vertDictionary:
        print(k, 'corresponds to: ', G.vertDictionary[k])

    v = 'a'
    nbrs = G.getNeighbors(v)
    for n in nbrs:
        print(n)
    print('\n')


def graphFromEdgelist(E,directed=False):
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])
    print('Vertices are: \n',V)

    verts = {}
    for v in V:
        verts[v] = g.addVertex(v)
    print('Num of Vertices: \n', g.vertexCount())

    for e in E:
        frm = e[0]
        to = e[1]
        weight = e[2] if len(e) > 2 else None
        g.addEdge(frm, to, weight)
    return g

if __name__ == '__main__':
    E = [('a','b',1),('a','c',2),('b','d',5)]
    graph = graphFromEdgelist(E,True)
    for k in graph.getEdges():
        print(k)
