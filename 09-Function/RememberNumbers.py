import random
import time
import os

#----------------------------------------------
#Functions
#----------------------------------------------
def ShowTheHelp():
    print("Welcome to the Game")
    print("In this game i show you sequence numbers in Limited Time")
    print("in each round , time will deacrease and game will dificultly ...")
    print("You Must remember the numbers and when the time ended , enter that numbers ")
    print("How many numbers can you guess ? ")
    print("---------------------------------------------------------------------------")     

#-----------------------------------------------
def SecondCounter(second):
    for i in range(10):
        print(f"The Game Start in {second} Seconds ......")
        time.sleep(1)
        second -= 1

#-----------------------------------------------
def ShowRandomNumber(level ,timerCounter ,randomNumbers):
    print("Level ",level)
    print("---------------------------------------------------------------------------")
    randomNumber = random.randint(0,9)
    randomNumbers.append(randomNumber)
    print(randomNumbers)
    print("---------------------------------------------------------------------------")
    time.sleep(timerCounter)

#-----------------------------------------------
def ClearConsole():
    if os.name == "nt":
            os.system("cls")
    elif os.name == "posix":
            os.system("clear")

#-----------------------------------------------
def PlayerChoice(randomNumbers):
     global playerNumber
     for i in range(len(randomNumbers)):
        print(f"{i+1} .enter a number(You Can also enter 'quit' and 'reset') = ")
        playerNumber = input()
        if playerNumber == "quit":
             exit()
        elif playerNumber == "reset":
             level = 1
             randomNumbers = []
             timerCounter = 5.0
             break
        else :
            player_Numbers.append(int(playerNumber))

#-----------------------------------------------
def CheckTheEndGame():
    if player_Numbers != randomNumbers:
        print(f"Your Numbers = {player_Numbers}")
        print(f"My Numbers = {randomNumbers}")
        print(f"Game Over! You played well , your level is {level}")
        return True
    return False
 
#-----------------------------------------------
level = 1
randomNumbers = []
timerCounter = 5.0
ShowTheHelp()
SecondCounter(10)

while True:
    ShowRandomNumber(level ,timerCounter ,randomNumbers)
    ClearConsole()
    player_Numbers = []
    PlayerChoice(randomNumbers)
    endGame = CheckTheEndGame()
    if endGame:
         break
    else:
        if randomNumbers != []:
            level += 1
        ClearConsole()
        timerCounter -= 0.25

    