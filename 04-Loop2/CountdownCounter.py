import time

print("Please Enter number of seconds for countdown = ",end="")
count = int(input())

while count >= 0:
    if count==0:
        print("Time's Up!")
        break
    print(count,"Seconds remainig ... ")
    time.sleep(1)
    count -= 1

