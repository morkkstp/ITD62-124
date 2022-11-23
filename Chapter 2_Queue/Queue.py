class Queue:
    # Method ใช้สร้าง Queue
    def __init__(self, n):
        self.n = n # กำหนดขนาดของ Queue
        self.queue = [] * n # การสร้างขนาดของ Queue
        self.front = -1 # กำหนด index front
        self.rear = -1 # กำหนด index rear

     # Method ตรวจสอบขนาดของ Queue
    def lenght(self):
        return len(self.queue)

    # Method การเพิ่มข้อมูลเข้าไปใน Queue
    def enqueue(self, item):
        if self.rear == self.n - 1:
            print("Queue is Full")
        else:
            if self.lenght() == 0: # ถ้าขนาดของ Queue เท่ากับ 0
                self.queue.append(item) # เพิ่มค่าเข้าไปที่ Queue ที่สร้างไว้
                self.front = 0 # กำหนด index front = 0
                self.rear = 0 # กำหนด index rear = 0
            else:
                self.rear = self.rear + 1 # เพิ่มตำแหน่ง rear
                self.queue.append(item) # เพิ่มค่าเข้าไปที่ Queue ที่สร้างไว้

    # Method การลบข้อมูลในตำแหน่ง front ใน Queue
    def dequeue(self):
        if self.lenght() == 0:
            print("Queue is Empty")
        else:
            self.queue.pop(self.front)
            self.front = self.front + 1 # เพิ่มตำแหน่ง front

    # Method แสดงข้อมูลใน Queue
    def display(self):
        print("Queue = ", end = " ")
        print(self.queue)

class CircularQueue:
    # Method ใช้สร้าง CircularQueue
    def __init__(self, n):
        self.n = n # กำหนดขนาดของ Queue
        self.queue = [] * n # การสร้างขนาดของ Queue
        self.front = -1 # กำหนด index front
        self.rear = -1 # กำหนด index rear

    # Method การเพิ่มข้อมูลเข้าไปใน CircularQueue
    def enqueue(self, data):
        if ((self.rear + 1) % self.n == self.front):
            print("Circular Queue is Full")
        elif (self.front == -1): # ถ้า index front ตรงกับตำแหน่ง -1
            self.front = 0 # กำหนด index front = 0
            self.rear = 0 # กำหนด index rear = 0
            self.queue.append(data) # เพิ่มค่าเข้าไปที่ CircularQueue ที่สร้างไว้
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue.append(data) # เพิ่มค่าเข้าไปที่ CircularQueue ที่สร้างไว้

    # Method การลบข้อมูลในตำแหน่ง front ใน CircularQueue
    def dequeue(self):
        if (self.front == -1):
            print("Circular Queue is Empty")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            return temp
    
    # Method แสดงข้อมูลใน CircularQueue
    def display(self):
        if (self.front == -1): # ถ้า index front ตรงกับตำแหน่ง -1
            print("No element in the Circular Queue")
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.front, self.n):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
