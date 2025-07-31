import random

#----------------------------------------------
#Functions
#----------------------------------------------
def Show_WordLetterList(list):
    for letter in list:
        print(letter,end="")

#---------------------------------------------
def CheckTheGame(chance ,wordLetterList):
    if chance == 0:
        print("\n😣 You Lose!")
        return True
    if '-' not in wordLetterList:
        print("\n🥳 You Win !")
        return True
    return False

#-----------------------------------------------
def CheckTheGuessLetter(guess ,chance ,wordLetterList):
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
difficulty = input("Choose difficulty (Hard/Easy): ").lower()
easyList = ['cat','dog','pen','book','eye','foot','ram','cpu','hard','easy']
hardList = ["sajjad","programmer","computer","phone","mobile","laptop","keyboard","python","graphic"]
#MyWords = ["sajjad","programmer","computer","phone","mobile","mouse","laptop","keyboard","python","graphic","ram","cpu","hard"]
if difficulty == "easy":
    word = random.choice(easyList)
else:
    word = random.choice(hardList)
randomWord = word
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