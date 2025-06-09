import random

#----------------------------------------------
#Functions
#----------------------------------------------
def Show_WordLetterList(list):
    for letter in list:
        print(letter,end="")

#---------------------------------------------
def CheckTheGame(chance ,list):
    if chance == 0:
        print("\n😣 You Lose!")
        return True
    if '-' not in wordLetterList:
        print("\n🥳 You Win !")
        return True
    return False

#-----------------------------------------------
def CheckTheGuessLetter(guess ,word ,chance ,list):
    guess = guess.lower()
    if guess in randomWord :
        for i in range(len(randomWord)):
            if guess == randomWord[i]:
                wordLetterList[i] = guess
        print("✅")
        return chance
    else:
        chance -= 1
        print("❌")
        return chance

#----------------------------------------------------
MyWords = ["sajjad","programmer","computer","phone","mobile","mouse","laptop","keyboard","python","graphic","ram","cpu","hard"]
randomWord = random.choice(MyWords)
chance = len(randomWord)
print("Welcome to the Game !")
wordLetterList = ['-'] * chance

while chance >= 0:
    print("\nYour Choice Count = ",chance)
    Show_WordLetterList(wordLetterList)
    checkGame = CheckTheGame(chance ,wordLetterList)
    if checkGame:
        break
    print("\nGuess the letter : ",end="")
    guess = input()
    if guess == "":
        print("Please Enter a letter ...")
    else:
        chance = CheckTheGuessLetter(guess ,randomWord ,chance ,wordLetterList)

print("End The Game ..... Thank's For Play , Come Back Again !")