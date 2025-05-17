#Import Math Class To use Power Function for Calculate the Area and PI function For a more accurate calculation
import math
#Get input from user
print("Please Enter Your Radius = ")
radius = int(input())
#Process
primeter = (radius * 2) * math.pi
area = math.pow(radius,2) * math.pi
#also Write The Area Code : radius ** 2 * math.pi
#also Write The Area Code : radius * radius * math.pi
print("Primeter = ",primeter)
print("Area = ",area)
