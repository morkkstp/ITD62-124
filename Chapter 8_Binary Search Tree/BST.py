# ประกาศ class Node และ Method __init__ เพื่อสร้าง node ใน BST(Binary search tree)
class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    # Method เพิ่ม node ใน Binary search tree
    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.leftChild == None:
                self.leftChild  = Node()
                self.leftChild.data  = data
            else:
                self.leftChild.insert(data)
        elif data > self.data:
            if self.rightChild == None:
                self.rightChild  = Node()
                self.rightChild.data  = data
            else:
                self.rightChild.insert(data)

    # Method หาค่าน้อยที่สุดใน BST(Binary search tree)
    def findMinimumValue(self):
        if self.leftChild == None:
            return self.data
        return self.leftChild.findMinimumValue()
    
BST = Node()