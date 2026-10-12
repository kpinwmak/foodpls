mainFoodlist = ['จานเดียว','ผัดและทอด','ต้มและแกง','ยำ/ตำ']
sFoodlist = ["กะเพราหมูสับ/ไก่ไข่ดาว","ผัดซีอิ๊วหมู/ไก่","ข้าวผัดหมู/ไก่","ข้าวหน้าไก่/หมูทอดกระเทียม","ผัดพริกแกงหมู/ไก่"]
fFoodlist = ["ไข่เจียวหมูสับ","ผัดผักบุ้งไฟแดง","ปลาทอดน้ำปลา/ทอดสามรส","กุ้งผัดพริกเกลือ/ผัดผงกะหรี่","ผัดคะน้าหมูกรอบ"]
wFoodlist = ["ต้มยำกุ้ง/ทะเล","ต้มจืดเต้าหู้หมูสับ","แกงเขียวหวานไก่"]
sfoodstock = []
ffoodstock = []
wfoodstock = []

print("date")
day = int(input("วันที่ : "))
month = str(input("เดือน (ตัวเลข 1-12) : "))
year = int(input("ปี : "))

print(f"----Food Stock----")

print(f"\n[เพิ่มสต็อกหมวด: {mainFoodlist[0]}]")
for i in sFoodlist :
        pstock = int(input(f"{i} : "))
        sfoodstock.append(pstock)
go = str(input("ไปต่อ y,n : "))
if go == "y":
    print(f"\n[เพิ่มสต็อกหมวด: {mainFoodlist[1]}]")
    for i in sFoodlist :
                pstock = int(input(f"{i} : "))
                ffoodstock.append(pstock)
    go2 = str(input("ไปต่อ y,n : "))
    if go2 == "y":
            print(f"\n[เพิ่มสต็อกหมวด: {mainFoodlist[2]}]")
            for i in wFoodlist :
                    pstock = int(input(f"{i} : "))    
                    wfoodstock.append(pstock)
    elif go2 == "n":
                     wfoodstock = [0,0,0]
elif go == "n":
        ffoodstock = [0,0,0,0,0]
        wfoodstock = [0,0,0]


soldsfoodlist = []
soldffoodlist = []
soldwfoodlist = []

print(f"\n---- Sold Food ----")

print(f"[Sold Food] หมวดที่ 1: {mainFoodlist[0]}")
for idx, i in enumerate(sFoodlist):
    soldsfood = int(input(f"{i} in stock {sfoodstock[idx]} sold : "))
    sfoodstock[idx] -= soldsfood  # หักลบจากสต็อกจานเดียว
    soldsfoodlist.append(soldsfood)

go = str(input("ไปต่อหมวดผัดและทอด? (y/n) : "))
if go == "y":
    print(f"\n[Sold Food] หมวดที่ 2: {mainFoodlist[1]}")
    for idx, i in enumerate(fFoodlist):
        soldsfood = int(input(f"{i} in stock {ffoodstock[idx]} sold : "))
        ffoodstock[idx] -= soldsfood  # หักลบจากสต็อกผัดและทอด
        soldffoodlist.append(soldsfood)
        
    go2 = str(input("ไปต่อหมวดต้มและแกง? (y/n) : "))
    if go2 == "y":
        print(f"\n[Sold Food] หมวดที่ 3: {mainFoodlist[2]}")
        for idx, i in enumerate(wFoodlist):
            soldsfood = int(input(f"{i} in stock {wfoodstock[idx]} sold : "))
            wfoodstock[idx] -= soldsfood  # หักลบจากสต็อกต้มและแกง
            soldwfoodlist.append(soldsfood)
    elif go2 == "n":
        soldwfoodlist = [0] * len(wFoodlist)
elif go == "n":
    soldffoodlist = [0] * len(fFoodlist)
    soldwfoodlist = [0] * len(wFoodlist)





# --- แสดงผลสรุป ---



print("\n================ สรุปการขายประจำวัน ================")

# 1. หมวดจานเดียว
print(f"\n<--- {mainFoodlist[0]} --->")
for idx, i in enumerate(soldsfoodlist):
    print(f"- {sFoodlist[idx]} : ขายได้ {soldsfoodlist[idx]} จาน | เหลือ {sfoodstock[idx]} จาน")

# 2. หมวดผัดและทอด (ถ้ามีการขาย)
if soldffoodlist:
    print(f"\n<--- {mainFoodlist[1]} --->")
    for idx, i in enumerate(soldffoodlist):
        print(f"- {fFoodlist[idx]} : ขายได้ {soldffoodlist[idx]} จาน | เหลือ {ffoodstock[idx]} จาน")

# 3. หมวดต้มและแกง (ถ้ามีการขาย)
if soldwfoodlist:
    print(f"\n<--- {mainFoodlist[2]} --->")
    for idx, i in enumerate(soldwfoodlist):
        print(f"- {wFoodlist[idx]} : ขายได้ {soldwfoodlist[idx]} จาน | เหลือ {wfoodstock[idx]} จาน")

































