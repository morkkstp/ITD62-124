# การประกาศคลาส Node
class Node:    
    def __init__(self, info = None):
        self.info = info
        self.next = None

# การประกาศคลาส Singly linked list และ Method เพื่อสร้าง object ให้มีรูปแบบคลาส Singly linked list
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # การประกาศ Method เพื่อเพิ่ม Node ที่จุดเริ่มต้นของ Singly linked list
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

    # การประกาศ Method เพื่อเพิ่ม Node ที่จุดสิ้นสุดของ Singly linked list
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