#The Triangle Inequality Theorim
print("Please Enter a First Side of the Triangle = ")
side1 = int(input())
print("Please Enter a Second Side of the Triangle = ")
side2 = int(input())
print("Please Enter a Third Side of the Triangle = ")
side3 = int(input())

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Yes , True , This is Possible to draw such a triangle ")
else:
    print("No , False , This is impossible to draw such a triangle ")

