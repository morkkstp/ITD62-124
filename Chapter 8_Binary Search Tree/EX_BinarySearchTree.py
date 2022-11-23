# ตัวอย่างการประกาศ class Node และ method __init__  เพื่อสร้าง node ใน Binary search tree
class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    # ตัวอย่าง method เพิ่ม node ใน Binary search tree
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

    # ตัวอย่าง method หาค่าน้อยที่สุดใน Binary search tree
    def findMinimumValue(self):
        if self.leftChild == None:
            return self.data
        return self.leftChild.findMinimumValue()

BST = Node()