### Assignment 8 : หาผลรวมตัวเลข

##################################################################################
# 1+2+3+4+5
i = 1 # ค่าเริ่มต้น
summation = 0 # เก็บผลการบวกเลขตามจำนวนรอบ
# หาค่าเฉลี่ยด้วย
average = 0 # ผลรวมหารด้วยจำนวนรอบ 
count=int(input("ระบุจำนวนรอบ : "))

while i<=count:
    summation+=i # เก็บผลรวมของ i แต่ละรอบ 1 + 2 + 3 + 4 + 5
    print("ค่า sum รอบที่", i , "= " , summation)
    i+=1

average = summation/count
print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ", average)
##################################################################################