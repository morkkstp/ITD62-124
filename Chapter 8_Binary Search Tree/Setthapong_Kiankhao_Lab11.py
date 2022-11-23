# สร้าง class Node เพื่อใช้ใน BST(Binary search tree)
class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    # Method เพิ่ม node ใน BST(Binary search tree)
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

    # Method หาค่ามากที่สุดใน BST(Binary search tree)
    def findMaximumValue(self):
        if self.rightChild == None:
            return self.data
        return self.rightChild.findMaximumValue()

    # Method เพื่อท่องไปในต้นไม้ในแบบ Post-order 
    def PostOrder(self, tree): 
        if tree: 
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            print(tree.data, end = " ")

BST = Node()
print("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บใน Binary search tree ถ้าไม่ต้องการเพิ่มข้อมูลอีกให้ป้อนค่าตัวเลข 12345")
i = True
# Loop สำหรับการรับข้อมูลจำนวนเต็มเพื่อจัดเก็บใน BST(Binary search tree)
while i == True:
    # รับข้อมูลเก็บในตัวแปร data
    data = int(input("ข้อมูล = "))
    # ถ้า data มีค่าเท่ากับ 12345 ให้ i มีค่าเป็น False
    if data == 12345:
        i = False
    else:
        # ใช้ Function insert() โดยส่ง argument คือ data เพื่อเพิ่ม node ใน BST(Binary search tree)
        BST.insert(data)
print("ผลลัพธ์จากการท่องไปใน Binary search tree ด้วยขั้นตอนวิธีแบบ Post-order")
# ใช้ Function PostOrder() เพื่อท่องไปในต้นไม้ในแบบ Post-order 
BST.PostOrder(BST)
# แสดงข้อความโดยใช้ Function findMaximumValue() เพื่อแสดงจำนวนเต็มมากที่สุดที่จัดเก็บใน BST(Binary search tree)
print("\nจำนวนเต็มมากที่สุดจัดเก็บใน Binary search tree คือ", BST.findMaximumValue())