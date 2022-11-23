# Function การเพิ่ม data และ ตรวจสอบการ Collision
def addData(data, key, sthash):
    # นำค่า key และ ค่าขนาดตารางแฮช(sthash) มาหาค่า index โดยการ Mod
    mod = key % sthash
    # ตรวจสอบว่าค่าในตารางแฮช มีค่าเท่ากับ None หรือไม่
    if hash[mod] == None:
        # แทนที่ค่าจาก data ไปที่ index ที่หาค่าจากการ Mod
        hash[mod] = data
    else:
        print("จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะตำแหน่งดังกล่าวในตารางแฮชจัดเก็บข้อมูล",hash[mod])
        # return True เพื่อการตรวจสอบค่า Collision ในบรรทัดที่ 30
        return True

# รับค่าขนาดตารางแฮช
sthash = int(input("โปรดป้อนขนาดตารางแฮช : "))
# ตารางแฮช
hash = [None] * sthash

# ตัวแปรที่เก็บการชนของข้อมูลในตารางแฮช
collision = 0
i = True
# รับค่า key
key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป: "))
# รับค่า data
data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช: ")
while i == True:
    # ตรวจสอบว่า key มีค่ามากกว่า 0 หรือไม่
    if key >= 0:
        # ตรวจสอบการชนว่าเป็นจริงหรือไม่
        if addData(data, key, sthash) == True:
            collision += 1
        # รับค่า key
        key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป: "))
        # รับค่า data
        data = input("โปรดป้อนค่าคีย์ (data) ที่เป็นข้อความเพื่อจัดเก็บข้อมูลในคารางแฮช: ")
    else:
        # ถ้า key มีค่าน้อยกว่า 0 ก็จะปรับให้ i เป็น False
        i = False

print("\nข้อมูลที่จัดเก็บในตารางแฮช")
# For Loop เพื่อแสดงข้อมูลในตารางแฮช
for i in range(sthash):
    # ตรวจสอบว่า hash[i] มีค่าเท่ากับ None หรือไม่
    if hash[i] == None:
        # ถ้าเป็นจริงก็ให้เปลี่ยนค่า None เป็น "ไม่มีข้อมูลจัดเก็บ" เพื่อการแสดงผล
        hash[i] = "ไม่มีข้อมูลจัดเก็บ"
    else:
        # ถ้าเป็นเท็จก็ให้เปลี่ยนเป็น "ข้อมูลคือ {}".format(hash[i]) เพื่อการแสดงผลโดยใช้ format และอ้างอิงค่า hash[i] จากตารางแฮช
        hash[i] = "ข้อมูลคือ {}".format(hash[i])
    # แสดงค่าแฮชโดยมีค่า index และ data ในตารางแฮช
    print("index {} , {}".format(i, hash[i]))
# แสดงค่า Collision
print("\nจำนวนครั้งที่เกิด Collision = {}".format(collision))