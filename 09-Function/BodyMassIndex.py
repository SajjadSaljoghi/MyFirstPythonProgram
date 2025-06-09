#BMI Program
import math

def calculate_BMI(weight ,height):
    bmi = weight / (math.pow(height/100,2))
    if bmi < 18.5:
        return f"BMI = {bmi}\nUnderweight!"
    elif bmi >= 18.5 and bmi < 25:
        return f"BMI = {bmi}\nNormal Weight"
    elif bmi >= 25 and bmi < 30:
        return f"BMI = {bmi}\nOverweight"
    elif bmi >= 30 and bmi < 35:
        return f"BMI = {bmi}\nObesity"
    else:
        return f"BMI = {bmi}\nExtreme Obesity"

print("Please Enter Your Weight(kg) = ")
weight = float(input())
print("Please Enter Your Height(cm) = ")
height = float(input())

user_BMI = calculate_BMI(weight ,height)
print(user_BMI)