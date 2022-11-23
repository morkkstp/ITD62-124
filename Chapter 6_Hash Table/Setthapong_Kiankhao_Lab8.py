# Function การเพิ่ม data ใน Index
def addData(key, data, sthash):
    # กำหนดค่า f(การชน) เท่ากับ 0
    f = 0
    # ถ้าค่าใน Index มีค่าเท่ากับ None
    if hash[key] == None:
        # แทนที่ค่าจาก data ไปที่ index ที่หาค่าจากการ Mod
        hash[key] = data
        print("Address = ",key)
    # ส่วนของ else คือ Hash Function 2
    else:
        # บวกการชนเพิ่มไปในตัวแปร f(การชน) ไป 1
        f += 1
        # สูตรคำนวณแบบ Linear probing
        h = (key + f) % sthash
        # ค่า key จะมีค่าเท่ากับ h ที่ได้จากการคำนวณแบบ Linear probing
        key = h
        # ใช Function แบบ Recursive Function
        addData(key, data, sthash)

# ป้อนขนาดตารางแฮช
sizehash = int(input("โปรดป้อนขนาดตารางแฮช : "))
# ตารางแฮช
hash = [None] * sizehash

i = True
while i == True:
    # รับค่า key
    key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่ามากกว่าหรือเท่ากับ 0: "))
    # รับค่า data
    data = input("โปรดป้อนข้อมูลชื่อสินค้าเพื่อจัดเก็บในตารางแฮช: ")
    # ถ้าค่า key มีค่ามากกว่าหรือเท่ากับ 0 ถ้าเป็นจริงก็จะรันชุดคำสั่งใน if
    if key >= 0:
        # คำนวณเพื่อหาค่า Index คือ Hash Function 1
        mod = key % sizehash
        # ใช้ Function addData เพื่อตรวจสอบ
        addData(mod, data, sizehash)
    else:
        i = False

# แสดงผลข้อมูลในตารางแฮช
print("\nข้อมูลที่จัดเก็บในตารางแฮช")
for i in range(sizehash):
    # ตรวจสอบว่า hash[i] มีค่าเท่ากับ None หรือไม่
    if hash[i] == None:
        # ถ้าเป็นจริงก็ให้เปลี่ยนค่า None เป็น "ไม่มีข้อมูลจัดเก็บ" เพื่อการแสดงผล
        hash[i] = "ไม่มีข้อมูลจัดเก็บ"
    else:
        # ถ้าเป็นเท็จก็ให้เปลี่ยนเป็น "ข้อมูลที่จัดเก็บคือ {}".format(hash[i]) เพื่อใช้ในการแสดงผล
        hash[i] = "ข้อมูลที่จัดเก็บคือ {}".format(hash[i])
    print("Address = {} {}".format(i, hash[i]))