### Assignment 11: ค้นหาตัวเลขมากสุด / น้อยสุด

##################################################################################
### ให้ทำงานใน loop while และป้อนตัวเลขเข้ามา

max, min = 0,9999 # set ค่าเริ่มต้น

while True:
    number = int(input("ป้อนตัวเลขของคุณ : "))
    # กระโดดออกจาก Loop
    if number<0:
        break
    if number>max:
        max=number
    if number<min:
        min=number

print("ค่าสูงสุด = ",max)
print("ค่าต่ำสุด = ",min)
print("End")

##################################################################################