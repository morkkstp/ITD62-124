# ประกาศ class ชื่อ Node
class Node:
    # ประกาศ Method ชื่อ __init__ เพื่อสร้าง Node
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    # ประกาศ Method ชื่อ insert เพื่อเพิ่ม Node ในต้นไม้
    def insert(self, data):
        if data != " ":
            self.data = data
        else:
            return
        
        # ป้อนค่าเพื่อจัดเก็บที่โหนด Left child
        data = input("โปรดป้อนข้อความเพื่อจัดเก็บที่โหนด Left child ของ "+ self.data +" (ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง): ")
        if data != " ":
            self.left = Node()
            self.left.data = data
            # Recursive Function ป้อนค่าเพื่อจัดเก็บที่โหนด Left child
            self.left.insert(data)

        # ป้อนค่าเพื่อจัดเก็บที่โหนด Right child
        data = input("โปรดป้อนข้อความเพื่อจัดเก็บที่โหนด Right child ของ "+ self.data +" (ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง): ")
        if data != " ":
            self.right = Node()
            self.right.data = data
            # Recursive Function ป้อนค่าเพื่อจัดเก็บที่โหนด Right child
            self.right.insert(data)

    # ประกาศ Method ชื่อ inOrder เพื่อท่องไปในต้นไม้ในแบบ In-order
    def inOrder(self, tree):
        if tree:
            self.inOrder(tree.left)
            print(tree.data)
            self.inOrder(tree.right)

    # ประกาศ Method ชื่อ postOrder เพื่อท่องไปในต้นไม้ในแบบ Post-order 
    def postOrder(self, tree):
        if tree:
            self.postOrder(tree.left)
            self.postOrder(tree.right)
            # ตรวจสอบเงื่อนไขว่า Node มีตัวอักษรที่ขึ้นต้นด้วย a, e, i, o, u โดยใช้ startswith
            if tree.data.startswith("a"):
                print(tree.data)
            elif tree.data.startswith("e"):
                print(tree.data)
            elif tree.data.startswith("i"):
                print(tree.data)
            elif tree.data.startswith("o"):
                print(tree.data)
            elif tree.data.startswith("u"):
                print(tree.data)

# รับค่า Root
data = input("โปรดป้อนข้อความเพื่อจัดเก็บที่ Root node : ")
# ประกาศ Class Node และเก็บในตัวแปร tree
tree = Node()
# ใช้ Function insert() โดยใส่ parameter data เข้าไป
tree.insert(data)
# ใช้ Function inorder() โดยใส่ parameter tree เข้าไป
print("ผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ In-order :")
tree.inOrder(tree)
# ใช้ Function postOrder() โดยใส่ parameter tree เข้าไป
print("\nผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ Post-order โดยแสดงข้อความที่จัดเก็บในแต่ละโหนดที่ขึ้นต้นด้วยอักษร a หรือ e หรือ i หรือ o หรือ u :")
tree.postOrder(tree)