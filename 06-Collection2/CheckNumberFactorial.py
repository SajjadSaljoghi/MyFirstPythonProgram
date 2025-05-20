print("Please Enter a Number = ",end="")
userNumber = int(input())

if userNumber <= 0:
    print("You Must enter a number that grater than 0")
else :
    fact = 1
    counter = 1

    while True:
        if fact == userNumber:
            print("Yse , The Number is a Factorial ")
            break
        elif fact > userNumber:
            print("No , the Number is not a Factorial ")
            break
        else:
            counter += 1
            fact = fact * counter
            #fact *= counter
