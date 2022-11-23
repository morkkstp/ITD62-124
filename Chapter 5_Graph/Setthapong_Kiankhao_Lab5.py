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
                    print("ระยะทางที่สั้นที่สุดจากจุดเริ่มต้นในการท่องไปในกราฟไปยังจุด ",nbr.getId(), " = ", nbr.getDistance())
            currentVertex.setColor('black')

graph = Graph()
# amount รับค่าจำนวนจุดในกราฟ
amount = int(input("โปรดระบุจำนวนจุดในกราฟ: "))

# Loop เพื่อรับค่า Vertex
for a in range(amount):
    vertex = input("โปรดระบุชื่อ Vertex: ")
    graph.addVertex(vertex)

# รับค่า Source และ Destination ของเส้นเชื่อม
print("โปรดระบุชื่อจุดที่เป็น source และ destination ของเส้นเชื่อม")
source = input("source = ")
destination = input("destination = ")
graph.addEdge(source, destination)

# Loop เพื่อรับค่า Source และ Destination ของเส้นเชื่อม
r = 1
while r == 1:
    print("โปรดระบุชื่อจุดที่เป็น source และ destination ของเส้นเชื่อม")
    source = input("ชื่อจุดที่เป็น source = ")
    destination = input("ชื่อจุดที่เป็น destination = ")
    # ถ้า Source และ Destination มีค่าเท่ากับ "-" ก็จะทำการ Break
    if source == "-" and destination == "-":
        r = 0
        break
    # ใช้ Method addEdge() โดยส่ง parameter = source,destination
    graph.addEdge(source, destination)

# รับค่าจุดเริ่มต้นที่ใช้ในการท่องไปในกราฟ โดยใช้ Method bfs() โดยส่ง parameter = start
print("โปรดระบุชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟด้วยขั้นตอนวิธีแบบ Breadth-first Search")
start = input("ชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟ = ")
graph.bfs(start)