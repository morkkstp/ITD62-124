class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph เป็นการจัดเก็บข้อมูลเส้นเชื่อมด้วย list ของเส้นเชื่อมที่มี 3 ค่า คือ u,v,w โดย u คือ source, v คือ destination, w คือ weight
        self.graph = []
    
    # ประกาศ Method addEdge เพื่อเพิ่มเส้นเชื่อมและเพิ่มข้อมูลใน list
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    # ประกาศ Method ชื่อ find_set
    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    # ประกาศ Method ชื่อ union
    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y 
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

    # ประกาศ Method Kruskal
    def kruskal(self):
        N = []
        self.graph = sorted(self.graph, key= lambda item: item[2])
        parent = []
        rank =[]
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent,u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                N.append([u, v, w])
                self.union(parent, rank, x, y)
        
        # การแสดงผลทั้งเส้นเชื่อมและผลรวมทั้งหมดของ Weight
        sumweight = 0
        for source, destination, weight in N:
            print("เส้นเชื่อมระหว่างจุด {} กับจุด {} มีค่าน้ำหนัก = {}".format(source, destination, weight))
            sumweight += weight
        print("Weight รวมของ Minimum spanning tree คือ {}".format(sumweight))

# รับค่าจำนวนจุดในกราฟแบบไม่มีทิศทาง
n = int(input("โปรดระบุค่าตัวแปร n (จำนวนจุดในกราฟแบบไม่มีทิศทาง (undirectef graph)): "))
graph = Graph(n)
# รับจำนวนเส้นเชื่อม (Edge)
edge = int(input("โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟแบบไม่มีทิศทาง : "))
print("โปรดระบุชื่อจุดที่เป็น Source ชื่อจุดที่เป็น Destination และค่าน้ำหนัก (Weight) ของเส้นเชื่อในกราฟ")
# For Loop เพื่อรับค่า Source, Destination, Weight
for e in range(edge):
    Source = int(input("Source = "))
    Destination = int(input("Destination = "))
    Weight = int(input("Weight = "))
    # เรียกใช้ Method addEdge เพื่อเพิ่มเส้นเชื่อมและเพิ่มข้อมูลใน list
    graph.addEdge(Source, Destination, Weight)
# เรียกใช้ Method kruskal
graph.kruskal()