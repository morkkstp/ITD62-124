# สร้าง class Node
class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

# สร้าง class Singly Linked List
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
        if self.head == None:
            print("LinkedList is empty")
        else:
            self.head = self.head.next

    # สร้าง Method เพื่อลบ Node ที่จุดสิ้นสุด
    def DeleteTheEnd(self):
        if self.tail == None:
            print("LinkedList is empty")
        else:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            self.tail = tmp
            self.tail.next = None
    
    # สร้าง Method เพื่อลบ Node ที่ต้องการ
    def DeleteSearch(self, data):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            tmp = self.head
            prev = self.head
            while tmp.info != data:
                prev = tmp
                tmp = tmp.next
            prev.next = tmp.next

    """def Display(self):
        if self.head == None:
            print("None")
        else:
            tmp = self.head
            while tmp.next != None:
                print(tmp.info, end=" ")
                tmp = tmp.next"""

    # สร้าง การแสดงผล
    def Display(self):
        if self.head == None: # ถ้า pointer head เท่ากับ None
            print("List is empty")
        else:
            tmp = self.head
            print("Singly Linked List:", end = " ")
            while tmp != None:
                print(tmp.info, end = " ")
                tmp = tmp.next

A = SLinkedList()
A.AtTheBeginning(3)
A.AtTheEnd(6)
A.AtTheEnd(74)
A.AtTheEnd(4)
A.Display()
A.DeleteBeginning()
print("\n")
A.Display()
A.DeleteSearch(74)
print("\n")
A.Display()