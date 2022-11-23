# ประกาศ Class Node
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 # ความสูงของ Node

# ประกาศ Class AVL tree
class AVL_Tree():
    # ประกาศ Method getHeight()
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # ประกาศ Method getBalance()
    def getBalance(self, root):
        if not root:
            return 0
        # หาค่าความต่างของความสูงด้านซ้ายและขวา
        return self.getHeight(root.left) - self.getHeight(root.right)

    # ประกาศ Method leftRotate()
    def leftRotate(self, z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # ประกาศ Method rightRotate()
    def rightRotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # ประกาศ Method insert()
    def insert(self, root, key):        
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        # ตรวจสอบความ Balanced เป็น Case 1 แบบ Single Rotation
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
        # ตรวจสอบความ Balanced เป็น Case 2 แบบ Double Rotation
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # ตรวจสอบความ Balanced เป็น Case 3 แบบ Double Rotation
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        # ตรวจสอบความ Balanced เป็น Case 4 แบบ Single Rotation
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
        return root

    # Method เพื่อท่องไปในต้นไม้ในแบบ Pre-order 
    def Pre_Order(self, root): 
        if root:
            print(root.data, end = " ")
            self.Pre_Order(root.left)
            self.Pre_Order(root.right)

AVL = AVL_Tree()
root = None
i = True
# Loop เพื่อรับค่า data เพิ่มไปใน Tree
while i == True:
    data = int(input("โปรดป้อนจำนวนเต็มเพื่อสร้าง AVL tree : "))
    # ถ้า data มีค่าเท่ากับ 9999 จะเปลี่ยนค่าในตัวแปร i จาก True เป็น False
    if data == 9999:
        i = False
    else:
        # เพิ่ม data และตรวจสอบความ Balanced และ Update ค่าในตัวแปร root เป็นค่าล่าสุดที่ input เข้ามา
        root = AVL.insert(root, data)
# แสดงผลรูปแบบ Pre-Order
print("ผลลัพธ์จากการท่องไปใน AVL tree ด้วยขั้นตอนวิธีเเบบ Pre-order")
AVL.Pre_Order(root)