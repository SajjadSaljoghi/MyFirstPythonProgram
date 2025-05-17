#in This File We Should be Calculate Time , get data from user and convert it to second 
print("Please Enter Your Hour : ")
hour = int(input())
print("Please Enter Your Minute : ")
minute = int(input())
print("Please Enter Your Second : ")
second = int(input())
#Process
if hour < 0 or hour > 24:
    print("Hour must bitween 0 - 24")
elif minute < 0 or minute > 59:
    print("Minute must bitween 0 - 59")
elif second < 0 or second > 59:
    print("Second must bitween 0 - 59")
else:
    result = (hour * 60 * 60) + (minute * 60) + second

print("Result is = ",result)
