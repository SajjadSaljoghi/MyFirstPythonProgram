print("Please Enter a Seconds Number to Convert hh:mm':ss'' = ")
secondsNumber = int(input())
hour = 0
minute = 0
second = 0

while True:
    if secondsNumber>=3600:
        secondsNumber = secondsNumber - 3600
        hour += 1
    elif secondsNumber<3600 and secondsNumber>=60:
        secondsNumber = secondsNumber - 60 
        minute += 1
    else:
        second = secondsNumber
        break

print("Time is : ",hour,":",minute,"':",second,"''")
        
