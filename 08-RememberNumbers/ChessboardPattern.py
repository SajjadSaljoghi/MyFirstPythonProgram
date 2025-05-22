print("Please Enter a number of the rows = ",end="")
row = int(input())
print("Please Enter a number of the columns = ",end="")
column = int(input())


for i in range(row):
    for j in range(column):
        if i % 2 == 0:
            if j % 2 == 0:
                print("⬜",end="")
            else:
                print("🟩",end="")
        else:
            if j % 2 == 0:
                print("🟩",end="")
            else:
                print("⬜",end="")
    print("")

