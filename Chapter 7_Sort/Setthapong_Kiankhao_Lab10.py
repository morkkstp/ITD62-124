# Function ในการจัดเรียงข้อมูลแบบ ShellSort
def ShellSort(list, n):
    # การทำงานของ ShellSort คือ จะจัดเรียงข้อมูลไปเรื่อยๆจนกว่า gapsize เหลือ 1
    flag = 1
    gapsize = n # เก็บค่า n ไปในตัวแปร gapsize
    while flag == 1 or gapsize > 1: # เป็นการวนซ้ำถ้า flag == 1 or gapsize > 1 เป็นจริง
        flag = 0
        gapsize = int((gapsize + 1)/2) # หา gapsize โดยใช้สูตร (gapsize + 1)/2
        for i in range(n - gapsize): # Loop ในการจัดเรียงข้อมูล
            if list[i + gapsize] < list[i]: # ตรวจสอบค่า
                list[i], list[i + gapsize] = list[i + gapsize], list[i] # ทำการสลับค่าใน index ของ list
                flag = 0

# Function สำหรับการแสดงผลก่อนการจัดเรียงข้อมูลแบบ ShellSort
def DisplayBeforeSort(list):
    print("ข้อมูลก่อนเรียงลำดับ คือ")
    for l in list:
        print(l, end = " ")

# Function สำหรับการแสดงผลหลังการจัดเรียงข้อมูลแบบ ShellSort
def DisplayAfterSort(list):
    print("\nข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
    for l in list:
        print(l, end = " ")

listshell = [] 

num = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ: ")) # ตัวแปรรับจำนวนข้อมูลที่ต้องการเรียงลำดับ
print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")
for i in range(num): # For Loop สำหรับการวนการรับข้อมูล
    data = input("ข้อมูล : ")
    listshell.append(data) # เพิ่มข้อมูลไปใน List ที่ชื่อว่า listshell
DisplayBeforeSort(listshell) # Function สำหรับการแสดงผลก่อนการจัดเรียงข้อมูลแบบ ShellSort
ShellSort(listshell, num) # Function ในการจัดเรียงข้อมูลแบบ ShellSort
DisplayAfterSort(listshell)  # Function สำหรับการแสดงผลหลังการจัดเรียงข้อมูลแบบ ShellSort