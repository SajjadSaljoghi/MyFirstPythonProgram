print("Please Enter a List to Remove Duplicate elements from that (example = 2,3,4,5,7,...):",end="")
userList = input()

numbers = userList.split(',')

for item in numbers:
    if not item.isnumeric():
        print("You Must Enter Number in List ...")
        break

resultList = []
duplicateElements = set()

for item in numbers:
    if item in resultList:
        duplicateElements.add(item)
    else:
        resultList.append(item)


print("Outout List (Without Duplicates Removed) = ",resultList)




