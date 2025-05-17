print("Please Enter Number 1 = ")
number1 = int(input())
print("Please Enter Number 2 = ")
number2 = int(input())

gcd = 1
if number1 <= number2:
    smallNumber = number1
else:
    smallNumber = number2


for i in range(2,smallNumber + 1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i

print("The Greatest Common Divisor(GCD) = ",gcd)