while True:
    print("Please Enter the Length of the Snake = ",end=" ")
    length = int(input())

    pattern = []
    if length<=0:
        print("Eror ! The Length should be a number grater than 0 ...")
    else:
        for i in range(int(length)):
            if i % 2 == 0:
                pattern.append("*")
            else:
                pattern.append("#")
        print("Striped Snake Pattern = ",end="")
        for item in pattern:
            print(item,end="")
        
        break
