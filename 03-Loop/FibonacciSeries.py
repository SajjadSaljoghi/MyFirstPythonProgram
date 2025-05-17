print("Please Enter a number to show n'th first number of Fibonacci Series = ")
nth = int(input())

number1 = 0
number2 = 1
print(number1,number2,end=" ")
counter = 3
if nth >= 3:
    while True:
        number3 = number1 + number2
        print(number3,end=" ")
        if nth>=4 and nth!=counter:
            number1 = number2
            number2 = number3
            counter += 1
        else:
            break



