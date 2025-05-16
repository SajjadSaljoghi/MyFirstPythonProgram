#BMI Program
import math
print("Please Enter Your Weight(kg) = ")
weight = float(input())
print("Please Enter Your Height(cm) = ")
height = float(input())

bmi = weight / (math.pow(height/100,2))

if bmi < 18.5:
    print("BMI = ",bmi)
    print("Underweight!")
elif bmi >= 18.5 and bmi < 25:
    print("BMI = ",bmi)
    print("Normal Weight")
elif bmi >= 25 and bmi < 30:
    print("BMI = ",bmi)
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("BMI = ",bmi)
    print("Obesity")
else:
    print("BMI = ",bmi)
    print("Extreme Obesity")