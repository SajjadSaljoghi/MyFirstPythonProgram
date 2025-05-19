print("Please Enter a Number to Length of Array = ",end=" ")
length = int(input())

userList = []

for i in range(length):
    print(i+1,".",end="")
    number = int(input())
    userList.append(number)

isSorted = True
for i in range(length):
    if userList[i] <= userList[i+1]:
        isSorted = True
    else:
        isSorted = False
        break
    

if isSorted == True:
    print("The Array is Sorted.")
else:
    print("The Array is not Sorted !")