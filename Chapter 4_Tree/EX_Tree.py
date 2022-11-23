# ตัวอย่างการประกาศคลาสชื่อ Node ใน Binary tree และ เมธอดชื่อ init เพื่อสร้าง Node โดยไม่ได้กำหนดค่าหมายเลขของโหนด
class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    # ตัวอย่างการประกาศเมธอดชื่อ insert เพื่อเพิ่ม Node ใน Binary tree โดย data คือ ค่าหมายเลขของโหนดที่ต้องการเพิ่ม ถ้าไม่มีโหนดลูกด้านซ้ายหรือโหนดลูกด้านขวาให้ป้อนค่าหมายเลขของโหนดลูกเป็น -1 
    def insert(self, data):
        if data != -1:
            self.data = data
        else:
            return

        data = int(input())
        if data != -1:
            self.leftChild = Node()
            self.leftChild.insert(data)

        data = int(input())
        if data != -1:
            self.rightChild = Node()
            self.rightChild.insert(data)

    # ตัวอย่างการประกาศเมธอดชื่อ PreOrder เพื่อท่องไปในต้นไม้แบบทวิภาคแบบ Pre-order 
    def PreOrder(self, tree):
        if tree:
            print(tree.data)
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)

    # ตัวอย่างการประกาศเมธอดชื่อ InOrder เพื่อท่องไปในต้นไม้แบบทวิภาคแบบ In-order
    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            print(tree.data)
            self.InOrder(tree.rightChild)

    # ตัวอย่างการประกาศเมธอดชื่อ PostOrder เพื่อท่องไปในต้นไม้แบบทวิภาคแบบ Post-order 
    def PostOrder(self, tree): 
        if tree: 
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            print(tree.data)

# ตัวอย่างคำสั่งประกาศ object ชื่อ tree ให้มีชนิดเป็นคลาส Node 
tree = Node()