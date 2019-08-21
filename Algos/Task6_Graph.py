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
    def __init__(self, numVertices=10, directed=False):
        self.adjMatrix = [[None] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        self.directed = directed
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def addVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n):
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
        return None

    def addEdge(self, frm, to, cost=0):
        #print("from",frm, self.getVertex(frm))
        #print("to",to, self.getVertex(to))
        if self.getVertex(frm) is not None and self.getVertex(to) is not None:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            if not self.directed:
                # For directed graph do not add this
                self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
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
                    edges.append((vid, wid, self.adjMatrix[u][v]))
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
