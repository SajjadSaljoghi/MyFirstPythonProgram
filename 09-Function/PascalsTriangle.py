#----------------------------------------------
#Functions
#----------------------------------------------
triangleList = []
def generate(row):
    zeroList = []
    for i in range(row):
        zeroList.append(int(1))
        triangleList.append(list(zeroList))
    for i in range(row):
        for j in range(i):
            if j == 0 or j == row -1:
                continue
            else:
                triangleList[i][j] = triangleList[i-1][j] + triangleList[i-1][j-1]
    return triangleList

#----------------------------------------------
def Show(_triangleList):
    for i in range(len(_triangleList)):
        for j in range(i+1):
            if j == i:
                print(_triangleList[i][j],end="")
            else:
                print(f"{_triangleList[i][j]}, ",end="")
        print("\n")

#----------------------------------------------
userRow = int(input("Please Enter a row to generate Pascals Triangle = "))
userTriangleList = generate(userRow)
Show(userTriangleList)
