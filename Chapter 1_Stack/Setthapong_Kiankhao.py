stack = []

def isEmpty(stack): # ฟังก์ชั่นตรวจสอบว่า stack ว่างหรือไม่
    if len(stack) == 0:
        return 1
    else:
        return 0

def isFull(stack): # ฟังก์ชั่นตรวจสอบว่า stack เต็มหรือไม่
    if len(stack) == n:
        return 1
    else:
        return 0

def top(): # ฟังก์ชั่นแสดงค่าบนสุดของ Stack
    return stack[-1]

def push(item): # ฟังก์ชั่นเพิ่มค่าใน Stack
    return stack.append(item)

def pop(): # ฟังก์ชั่นดึงค่าบนสุดออกจาก Stack
    return stack.pop()

def display(): # ฟังก์ชั่นแสดงข้อมูลทั้งหมด, แสดงค่าที่มากที่สุด, แสดงค่าที่น้อยที่สุด, แสดงค่าเฉลี่ย
    print("ข้อมูลที่จัดเก็บทั้งหมด = ",stack) # แสดงข้อมูลทั้งหมดใน Stack
    print("ค่ามากที่สุด = ",max(stack)) # แสดงค่าที่มากที่สุด
    print("ค่าน้อยที่สุด = ",min(stack)) # แสดงค่าที่น้อยที่สุด
    sum = 0
    for i in stack: # Loop เพื่อที่จะหาผลรวมของ Stack
        sum += i
    print("ค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack = ",sum / len(stack)) # คำนวณและแสดงค่าเฉลี่ย

# รับขนาดของ Stack
n = int(input("โปรดระบุขนาดของ Stack ที่เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
while n == 0: # ตรวจสอบถ้า n เท่ากับ 0 ให้รับขนาดของ Stack ใหม่
    n = int(input("โปรดระบุขนาดของ Stack ที่เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
stack = [] * n
choose = 1
while choose > 0 and choose <= 4: # ตรวจสอบว่าได้เลือกทางเลือก 1 ถึง 4 หรือไม่
    print("โปรดระบุทางเลือกในการดำเนินการกับ Stack")
    print("1. PUSH")
    print("2. POP")
    print("3. Top of Stack")
    print("4. Display ข้อมูลที่จัดเก็บใน Stack, ค่ามากที่สุด, ค่าน้อยที่สุด, ค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack")
    choose = int(input("ทางเลือกในการดำเนินการ = ")) # รับทางเลือก 1 ถึง 4
    if choose == 1: # ถ้าทางเลือกเท่ากับ 1
        if isFull(stack) == 0: # ตรวจสอบว่าถ้าฟังก์ชั่น isFull() return ค่าให้เท่ากับ 0
            number = int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Stack = "))
            push(number)
        else:
            print("ไม่สามารถจัดเก็บข้อมูลใน Stack ได้เพราะ Stack เต็ม")
    if choose == 2: # ถ้าทางเลือกเท่ากับ 2
        if isEmpty(stack) == 0: # ตรวจสอบว่าถ้าฟังก์ชั่น isEmpty() return ค่าให้เท่ากับ 0
            pop()
        else:
            print("ไม่สามารถดึงข้อมูลออกจาก Stack เพราะไม่มีข้อมูลจัดเก็บใน Stack")
    if choose == 3: # ถ้าทางเลือกเท่ากับ 3
        if isEmpty(stack) == 0: # ตรวจสอบว่าถ้าฟังก์ชั่น isEmpty() return ค่าให้เท่ากับ 0
            print("Top of Stack = ",top())
        else:
            print("ไม่สามารถแสดงค่า Top of Stack เพราะไม่มีข้อมูลจัดเก็บใน Stack")
    if choose == 4: # ถ้าทางเลือกเท่ากับ 4
        if isEmpty(stack) == 0: # ตรวจสอบว่าถ้าฟังก์ชั่น isEmpty() return ค่าให้เท่ากับ 0
            display()
        else:
            print("ไม่สามารถดำเนินการได้เพราะไม่มีข้อมูลจัดเก็บใน Stack")