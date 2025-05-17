print("Please Enter Your Shape to Show Stars ✨ = 1.Square 2.Triangle 3.Diamond")
shape = int(input())
print("Please Enter a number to Show the Shape = ",end="")
number = int(input())

if shape == 1:
    for i in range(number):
        for j in range(number):
            print("✨",end="")
        print()
elif shape == 2:
    empty = number - 1
    for i in range(number):
        for j in range(i+1):
            if j==0:
                for k in range(empty):
                    print(" ",end="")
            print("✨",end="")
        print()
        empty -= 1
elif shape == 3:
    empty = number - 1
    row = 0
    for i in range(number * 2 - 1):
        if i < number:
            row += 1
        else:
            row -= 1
            if i == number:
                empty = 1
            else:
                empty += 1
        for j in range(row):
            if j==0:
                for k in range(empty):
                    print(" ",end="")
            print("✨",end="")
        print()
        if i < number:
            empty -= 1