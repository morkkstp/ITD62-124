# ประกาศ class ชื่อ Node และ Method ชื่อ init เพื่อสร้าง Node
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    # ประกาศ Method ชื่อ Insert เพื่อเพิ่ม Node ใน tree
    def Insert(self, data):
        data = int(input("Right: "))
        if data != -1:
            self.right = Node()
            self.right.data = data

        L_R = input("Input L/R: ")
        if L_R == "L":
            if self.left == None:   
                self.left = Node()
                self.left.data = data
                return
            else:
                self.Insert(data)
        elif L_R == "R":
            if self.right == None:
                self.right = Node()
                self.right.data = data
                return
            else:
                self.Insert(data)

    # ประกาศ Method ชื่อ PreOrder เพื่อท่องไปในต้นไม้ในแบบ Pre-order 
    def PreOrder(self, tree):
        if tree:
            print(tree.data)
            self.PreOrder(tree.left)
            self.PreOrder(tree.right)

    # ประกาศ Method ชื่อ InOrder เพื่อท่องไปในต้นไม้ในแบบ In-order
    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.left)
            print(tree.data)
            self.InOrder(tree.right)

    # ประกาศ Method ชื่อ PostOrder เพื่อท่องไปในต้นไม้ในแบบ Post-order 
    def PostOrder(self, tree): 
        if tree: 
            self.PostOrder(tree.left)
            self.PostOrder(tree.right)
            print(tree.data)

tree = Node()
tree.data = int(input("Root: "))
while True:
    choose = int(input("1/2/3/4: "))
    if choose == 1:
        tree.PreOrder(tree)
    elif choose == 2:
        tree.InOrder(tree)
    elif choose == 3:
        tree.PostOrder(tree)
    elif choose == 4:
        data = int(input("Input Data: "))
        tree.Insert(data)
    else:
        break