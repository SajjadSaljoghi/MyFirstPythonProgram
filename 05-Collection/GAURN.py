#this program G_enerate A_rray with U_nique R_andom N_umber (GAURN)

import random

print("Please Enter a Number to Length of Array (for generate unique random number) = ",end=" ")
length = int(input())

randomList = []

counter = 0
while True:
    if counter == length:
        break
    randomNumber = random.randint(0,length*length)
    numberExist = False
    for number in randomList:
        if number == randomNumber:
            numberExist = True
    if numberExist == False:
        randomList.append(randomNumber)
        counter += 1
    
print("Generate Array = ",randomList)