#In This File We Must Get FirstName , LastName and 3 Course Grades of a Student,Then Calculate Average and Print Students academic Status
print("Please Enter First Name = ")
firstName = input()
print("Please Enter Last Name = ")
lastName = input()
print("Please Enter Course Grade 1 = ")
grade1 = float(input())
print("Please Enter Course Grade 2 = ")
grade2 = float(input())
print("Please Enter Course Grade 3 = ")
grade3 = float(input())
#----------------------------------------------------------------
#Then Process Now ...
fullName = firstName + lastName
average = (grade1 + grade2 + grade3) / 3

if average >= 17:
    print("Mr/Mrs ",fullName," Wooooow! Perfect 😍,You're DistinGuished Student ")
elif average <17 or average >=12:
    print("Mr/Mrs ",fullName," Good ... You're Normal Student ")
else:
    print("Mr/Mrs ",fullName," Bad! That's Awful, You're Conditional Student ")