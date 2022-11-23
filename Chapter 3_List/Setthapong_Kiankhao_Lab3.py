# สร้าง class Node
class Node:
    def __init__(self, info = None): # กำหนด info ตั้งต้นให้เป็น None
        self.info = info
        self.next = None

# สร้าง class Singly LinkedList
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # สร้าง Method เพื่อเพิ่ม Node ที่จุดเริ่มต้น
    def AtTheBeginning(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    # สร้าง Method เพื่อเพิ่ม Node ที่จุดสิ้นสุด
    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode            
            self.tail = NewNode

    # สร้าง Method เพื่อลบ Node ที่จุดเริ่มต้น
    def DeleteTheBeginning(self):
        if self.head == None: # ถ้า pointer head เท่ากับ None
            print("ไม่สามารถลบข้อมูลได้เพราะ Linked List ว่าง")
        elif self.tail == self.head: # ถ้า pointer tail ตรงกับ pointer head
            self.head = None # pointer head ก็จะเป็น None
            self.tail = None # pointer tail ก็จะเป็น None
        else:
            self.head = self.head.next # pointer head ก็จะอยู่ Node ถัดไป

    # สร้าง Method เพื่อลบ Node ที่จุดสิ้นสุด
    def DeleteTheEnd(self):
        if self.tail == None: # ถ้า pointer tail เท่ากับ None
            print("ไม่สามารถลบข้อมูลได้เพราะ Linked List ว่าง")
        elif self.tail == self.head: # ถ้า pointer tail ตรงกับ pointer head
            self.head = None # pointer head ก็จะเป็น None
            self.tail = None # pointer tail ก็จะเป็น None
        else:
            tmp = self.head # เก็บค่าของ Node pointer head ในตัวแปร tmp
            while tmp.next != self.tail: # ถ้าตำแหน่งของ Node pointer head ไม่เท่ากับ pointer
                tmp = tmp.next # ขยับ Node pointer head
            self.tail = tmp
            self.tail.next = None # ปรับ tail.next เป็น None
    
    # สร้าง Method เพื่อลบ Node ที่ต้องการ
    def DeleteSearch(self, data):
        if self.head == None: # ถ้า pointer head ไม่เท่ากับ None
            print("ไม่มีข้อมูลที่ต้องการลบใน Linked List")
        else:
            tmp = self.head # เก็บค่าของ Node pointer head ในตัวแปร tmp
            prev = self.head # เก็บค่าของ Node pointer head ในตัวแปร prev
            tail = self.tail # เก็บค่าของ Node pointer tail ในตัวแปร tail
            if tmp.info == data: # ถ้า pointer head เท่ากับ data ที่รับมา
                self.DeleteTheBeginning() # เรียกใช้ Method DeleteTheBeginning()
                return
            elif tail.info == data: # ถ้า pointer tail เท่ากับ data ที่รับมา
                self.DeleteTheEnd() # เรียกใช้ Method DeleteTheEnd()
                return
            while tmp.info != data: # ถ้าตำแหน่งของ Node pointer head ไม่เท่ากับ data
                if tmp.info != data and self.tail == tmp: # ถ้า Node ไม่เท่ากับ data และ pointer tail ไม่เท่ากับ pointer
                    print("ไม่มีข้อมูลที่ต้องการลบใน Linked List")
                    return
                prev = tmp
                tmp = tmp.next
            prev.next = tmp.next

    # สร้าง Method เพื่อการแสดงผลทางจอภาพ
    def Display(self):
        if self.head == None: # ถ้า pointer head เท่ากับ None
            print("ไม่สามารถแสดงข้อมูลได้เพราะ Linked List ว่าง")
        else:
            print("Head = {} Tail = {}".format(self.head.info, self.tail.info))
            display = self.head # เก็บ Node pointer head ไว้ที่ตัวแปร display
            while display != None: # ถ้าตัวแปร display 
                print("ข้อมูลที่จัดเก็บ =", display.info)
                display = display.next # ขยับไป Node ถัดไป

SLL = SLinkedList() # เรียกใช้ Class Singly Linked List
print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
print("1. เพิ่มข้อมูลที่จุดเริ่มต้น Singly linked list")
print("2. เพิ่มข้อมูลที่จุดสิ้นสุด Singly linked list")
print("3. ลบข้อมูลที่จุดเริ่มต้น Singly linked list")
print("4. ลบข้อมูลที่จุดสิ้นสุด Singly linked list")
print("5. ลบข้อมูลที่ระบุจาก Singly linked list")
print("6. แสดงข้อมูลจัดเก็บทั้งหมดใน Singly linked list")
choose = int(input("ทางเลือกในการดำเนินการ = ")) # เลือกทางเลือกในการดำเนินการ
while choose >= 1 and choose <= 6:
    if choose == 1: # ถ้าเลือก 1 จะใช้งานการเพิ่ม Node ที่จุดเริ่มต้น
        data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดเริ่มต้น Singly linked list = "))
        SLL.AtTheBeginning(data)
    elif choose == 2: # ถ้าเลือก 2 จะใช้งานการเพิ่ม Node ที่จุดสิ้นสุด
        data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดสิ้นสุด Singly linked list = "))
        SLL.AtTheEnd(data)
    elif choose == 3: # ถ้าเลือก 3 จะใช้งานการลบ Node ที่จุดเริ่มต้น
        SLL.DeleteTheBeginning()
    elif choose == 4: # ถ้าเลือก 4 จะใช้งานการลบ Node ที่จุดสิ้นสุด
        SLL.DeleteTheEnd()
    elif choose == 5: # ถ้าเลือก 5 จะใช้งานการลบ Node ที่ต้องการ
        data = int(input("ข้อมูลที่ต้องการลบจาก Singly linked list = "))
        SLL.DeleteSearch(data)
    elif choose == 6: # ถ้าเลือก 6 จะใช้งานการแสดงผลทางจอภาพ
        SLL.Display()
    else: # ถ้าไม่ได้เลือก 1 ถึง 6 ก็จะจบการทำงาน
        break
    print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
    print("1. เพิ่มข้อมูลที่จุดเริ่มต้น Singly linked list")
    print("2. เพิ่มข้อมูลที่จุดสิ้นสุด Singly linked list")
    print("3. ลบข้อมูลที่จุดเริ่มต้น Singly linked list")
    print("4. ลบข้อมูลที่จุดสิ้นสุด Singly linked list")
    print("5. ลบข้อมูลที่ระบุจาก Singly linked list")
    print("6. แสดงข้อมูลจัดเก็บทั้งหมดใน Singly linked list")
    choose = int(input("ทางเลือกในการดำเนินการ = ")) # เลือกทางเลือกในการดำเนินการ