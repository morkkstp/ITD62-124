class Queue:
    # Method ใช้สร้าง Queue
    def __init__(self, n):
        self.n = n # กำหนดขนาดของ Queue
        self.queue = [] * n # การสร้างขนาดของ Queue
        self.front = -1 # กำหนด index front
        self.rear = -1 # กำหนด index rear
        self.total = 0 # ใช้เก็บและแสดงผลรวมทั้งหมด
        self.better200 = 0 # ใช้เก็บและแสดงจำนวนตัวเลขที่มีค่ามากกว่า 200

    # Method ตรวจสอบขนาดของ Queue
    def lenght(self):
        return len(self.queue)

    # Method การเพิ่มข้อมูลเข้าไปใน Queue
    def enqueue(self, item):
        if self.rear == self.n - 1:
            print("Queue เต็ม")
        else:
            if self.lenght() == 0: # ถ้าขนาดของ Queue เท่ากับ 0
                self.queue.append(item) # เพิ่มค่าเข้าไปที่ Queue ที่สร้างไว้
                self.front = 0 # กำหนด index front = 0
                self.rear = 0 # กำหนด index rear = 0
                print("ข้อมูลที่ต้องการเพิ่ม :", item)
            else:
                self.rear = self.rear + 1 # เพิ่มตำแหน่ง rear
                self.queue.append(item) # เพิ่มค่าเข้าไปที่ Queue ที่สร้างไว้
                print("ข้อมูลที่ต้องการเพิ่ม :", item)

    # Method การดึงข้อมูลออกใน Queue
    def dequeue(self):
        if self.lenght() == 0:
            print("Queue ว่าง")
        else:
            if self.queue[n-1] != None: # ถ้า index สุดท้ายของ Queue ไม่เป็น None
                self.queue[self.front] = None # ปรับค่าในตำแหน่งให้เป็น None
                self.front = self.front + 1 # เพิ่มตำแหน่ง front
            else:
                print("Queue ว่าง")

    # Method แสดงข้อมูลใน Queue
    def display(self):
        if self.lenght() == 0:
            print("Queue ว่าง")
        else:
            print("", end = " ")
            print(self.queue)
    
    # Method แสดงข้อมูลผลรวมและจำนวนตัวเลขที่มีค่ามากกว่า 200
    def displaySumAndBetter200(self):
        if self.lenght() != 0: # ถ้าจำนวนใน Queue ไม่เท่ากับ 0
            self.db = [] # self.db ใช้เก็บค่าที่ไม่มี None
            for i in self.queue:
                if i != None: # ถ้า i ไม่เท่ากับ None
                    self.total += i
                    self.db.append(i) # เพิ่มค่าไปที่ self.db
            print("ผลรวม = ", self.total) # แสดงผลรวม
            for i in self.db:
                if i > 200:
                    self.better200 += 1
            print("จำนวนตัวเลขจำนวนเต็มที่มีค่ามากกว่า 200 = ", self.better200) # แสดงจำนวนตัวเลขที่มีค่ามากกว่า 200
            print("\nจบการทำงาน")
        else:
            print("ไม่สามารถแสดงผลรวมและจำนวนเต็มที่มีค่ามากกว่า 200 ได้เพราะ Queue ว่าง")
            print("\nจบการทำงาน")

n = int(input("โปรดระบุขนาดของ Queue = "))
while n <= 0:
    n = int(input("โปรดระบุขนาดของ Queue ที่มีค่ามากกว่า 0 = "))

queue = Queue(n) # สร้าง Queue
choose = 1 # กำหนดตัวแปร choose = 1 เพื่อที่จะเข้า Loop While
# ถ้า choose มีค่ามากกว่าหรือเท่ากับ 1 และ choose มีค่าน้อยกว่าหรือเท่ากับ 3
while choose >= 1 and choose <= 3:
    print("\nโปรดระบุทางเลือกในการดําเนินการกับ queue")
    print("1. รับข้อมูลจํานวนเต็มจัดเก็บใน queue")
    print("2. ดึงข้อมูลจาก queue 1 ช่อง")
    print("3. แสดงข้อมูลที่จัดเก็บทั้งหมดใน queue ทางจอภาพ")
    choose = int(input("ทางเลือกในการดําเนินการ = ")) # รับค่าทางเลือก
    if choose == 1:
        # รับข้อมูลที่ต้องการจัดเก็บข้อมูลใน queue โดยเก็บไว้ในตัวแปร data
        data = int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน queue = "))
        queue.enqueue(data) # ใช้ Function โดยส่ง Argument ที่ชื่อว่า data
    elif choose == 2:
        queue.dequeue() # ใช้ Function เพื่อดึงข้อมูลออก
    elif choose == 3:
        queue.display() # ใช้ Function เพื่อแสดงข้อมูลที่จัดเก็บใน Queue ทางจอภาพ
    else:
        # เมื่อไม่ได้กดเลือกหมายเลข 1, 2, 3 ก็จะเรียกใช้ Function นี้
        # เพื่อแสดงข้อมูลผลรวมและจำนวนตัวเลขที่มีค่ามากกว่า 200
        queue.displaySumAndBetter200()
        break