# ประกาศ Class Graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # self.graph เป็นการจัดเก็บข้อมูลเส้นเชื่อมด้วย list ของเส้นเชื่อมที่มี 3 ค่า คือ u,v,w โดย u คือ source, v คือ destination, w คือ weight

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w]) # เมื่อมีการเพิ่มเส้นเชื่อมจะมีการเพิ่มข้อมูลใน list

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
        A = []
        self.graph = sorted(self.graph, key = lambda item: item[2])
        parent = []
        rank = []
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)

n = input("input: ")
g = Graph(n)