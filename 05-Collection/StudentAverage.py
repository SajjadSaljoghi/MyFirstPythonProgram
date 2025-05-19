grades = []
average = 0

while True:
    print("Enter a grade (or type 'exit' to finish) : ",end="")
    userGrade = input()
    if userGrade == "exit":
        break
    else:
        grades.append(float(userGrade))
        

sum = 0
for grade in grades:
    sum += grade


average = sum / len(grades)
print("Average GPA = ",average)