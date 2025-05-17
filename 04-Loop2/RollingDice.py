import random,time

print("Please Enter a Number Between 2 - 12 to rolling dice = (I have 2 dice) ")
programNumber = int(input())



while True:    
    randomDice1 = random.randint(1,6)
    randomDice2 = random.randint(1,6)
    sumOfDices = randomDice1 + randomDice2
    print("You rolled a ",randomDice1,"and a ",randomDice2," .Sum is ",sumOfDices)
    if sumOfDices == programNumber:
        print("Congratulation! 🥳 ... You Win")
        break
    else:
        print("Rolling the dices .... ")
        time.sleep(2)
        

