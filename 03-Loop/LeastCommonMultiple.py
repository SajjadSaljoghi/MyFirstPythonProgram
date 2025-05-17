print("Please Enter Number 1 = ")
number1 = int(input())
print("Please Enter Number 2 = ")
number2 = int(input())

largeNumber = 0
if number1 >= number2:
    largeNumber = number1
else:
    largeNumber = number2
multipleNumber = number1 * number2

for i in range(largeNumber,multipleNumber + 1):
    if i % number1 == 0 and i % number2 == 0:
        largeNumber = i
        break

print("The Least Common Multiple(LCM) = ",largeNumber)