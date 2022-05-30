# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง

# Input
weight = int(input("ป้อนน้ำหนักของคุณ (kg) :"))
height = int(input("ป้อนส่วนสูงของคุณ (cm) :"))

# process
# cm => m
height = height/100

# Calculate BMI
bmi = round(weight/(height**2),2)

# output
print("BMI = ",bmi)