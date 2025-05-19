userList = []

print("Please Enter a Number to Length of List = ",end=" ")
length = int(input())


for i in range(length):
    print(i+1,".",end="")
    number = int(input())
    userList.append(number)

reversedList = []
counter = len(userList) - 1
for i in range(len(userList)):
    reversedList.append(userList[counter])
    counter -= 1

print("Riversed List = ",reversedList)