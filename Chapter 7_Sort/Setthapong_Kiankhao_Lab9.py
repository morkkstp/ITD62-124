# Function ในการจัดเรียงข้อมูลแบบ BubbleSort
def BubbleSortAlgo(list):
    # การจัดเรียงข้อมูลแบบ BubbleSort
    for x in range(len(list)):
        for y in range(0, (len(list)-1)-x):
            if list[y] > list[y+1]: # ตรวจสอบการเปรียบเทียบค่า
                list[y], list[y+1] = list[y+1], list[y]

# Function สำหรับการแสดงผลก่อนการจัดเรียงข้อมูลแบบ BubbleSort
def DisplayBeforeSort(list):
    print("ข้อมูลก่อนเรียงลำดับ คือ")
    for l in list:
        print(l, end = " ")

# Function สำหรับการแสดงผลหลังการจัดเรียงข้อมูลแบบ BubbleSort
def DisplayAfterSort(list):
    print("\nข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
    for l in list:
        print(l, end = " ")

listSort = []

numsort = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ: ")) # ตัวแปรรับจำนวนข้อมูลที่ต้องการเรียงลำดับ
print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")
for i in range(numsort): # For Loop สำหรับการวนการรับข้อมูล
    data = int(input("ข้อมูล : "))
    listSort.append(data) # เพิ่มข้อมูลไปใน List ที่ชื่อว่า listSort
DisplayBeforeSort(listSort) # Function สำหรับการแสดงผลก่อนการจัดเรียงข้อมูลแบบ BubbleSort
BubbleSortAlgo(listSort) # Function ในการจัดเรียงข้อมูลแบบ BubbleSort
DisplayAfterSort(listSort) # Function สำหรับการแสดงผลหลังการจัดเรียงข้อมูลแบบ BubbleSort