import math
# สร้างคลาส queue เพื่อใช้ใน BFS 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

# สร้างคลาส Vertex 
class Vertex:
    def __init__(self,data):
        self.id = data
        self.distance = math.inf
        self.color = 'white'
        self.pred = None
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.distance = d

    def setPred(self,p):
        self.pred = p

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

# สร้างคลาส Graph
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices

    def addEdge(self,f,t):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t])

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

# ประกาศ method ชื่อ bfs เพื่อท่องไปในกราฟแบบ BFS 
    def bfs(self,start):
        s = self.getVertex(start)
        s.setDistance(0)
        s.setPred(None)
        q = Queue()
        q.enqueue(s)
        while not(q.isEmpty()):
            currentVertex = q.dequeue()
            for nbr in currentVertex.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVertex.getDistance() + 1)
                    nbr.setPred(currentVertex)
                    q.enqueue(nbr)
                print(nbr.getId(), ' = ', nbr.getDistance())
            currentVertex.setColor('black')

g = Graph()
