from termcolor import colored
#----------------------------------------------
#Functions
#----------------------------------------------
def multiply(row ,column):
    for i in range(0 ,row+1):
        for j in range(0 ,column+1):
            if i == 0 or j == 0:
                if j == 0:
                    result = colored(i,"blue")
                elif i == 0:
                    result = colored(j,"blue")
                print(result,end="")
                print("\t",end="")
            elif i == j:
                result = colored(j * i,"red")
                print(result,end="")
                print("\t",end="")
            else:
                print(i * j,end="")
                print("\t",end="")
        print("\n")

#-----------------------------------------------
row = int(input("Please Enter row = "))
column = int(input("Please enter column = "))
myMultiplyTable = multiply(row,column)
