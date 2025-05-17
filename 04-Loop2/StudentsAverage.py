print("Please Enter Your Course to calculate the average = ",end=" ")
courseCount = int(input())
print()

average = 0
courseSum = 0

for i in range(courseCount):
    print("Course ",i + 1," = ",end="")
    course = float(input())
    courseSum += course

average = courseSum / courseCount
print()
print("Average of ",courseCount," Course = ",average,end="")
