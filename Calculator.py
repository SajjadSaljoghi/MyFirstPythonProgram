#Calculator , There is Nothing to Say ....
import math

print("Please Enter Your Number 1 = ")
number1 = float(input())
print("Please Enter Your Number 2 = ")
number2 = float(input())
print("Please Enter Your operator (+ - * / ^ sqrt sin cos tan cot fact) = ")
operator = input()

if operator == "+":
    print("Sum = ",number1 + number2)
elif operator == "-":
    print("Subtraction = ",number1 - number2)
elif operator == "*":
    print("Multiply = ",number1 * number2)
elif operator == "/":
    if(number2 != 0):
        print("Divide = ",number1 / number2)
    else:
        print("Divide By Zero Can not be accepted ....")
elif operator == "^":
    print("Power = ",math.pow(number1,number2))
elif operator == "sqrt":
    print("Number1 or Number2 ? Please Enter 1 or 2")
    getNumber_for_Sqrt = int(input())
    if(getNumber_for_Sqrt == 1):
        print("Sqrt = ",math.sqrt(number1))
    else:
        print("Sqrt = ",math.sqrt(number2))
elif operator == "fact":
    print("Number1 or Number2 ? Please Enter 1 or 2")
    getNumber_for_fact = int(input())
    if(getNumber_for_fact == 1):
        print("Factorial = ",math.factorial(int(number1)))
    else:
        print("Factorial = ",math.factorial(int(number2)))
elif operator == "sin":
    print("Please Enter degree 0 - 360")
    degree = int(input())
    radian = math.radians(degree)
    print("Sin ",degree," = ",math.sin(radian))
elif operator == "cos":
    print("Please Enter degree 0 - 360")
    degree = int(input())
    radian = math.radians(degree)
    print("Cos ",degree," = ",math.cos(radian))
elif operator == "tan":
    print("Please Enter degree 0 - 360")
    degree = int(input())
    radian = math.radians(degree)
    print("Tan ",degree," = ",math.tan(radian))
elif operator == "cot":
    print("Please Enter degree 0 - 360")
    degree = int(input())
    radian = math.radians(degree)
    print("Cot ",degree," = ",1 / math.tan(radian))

    

