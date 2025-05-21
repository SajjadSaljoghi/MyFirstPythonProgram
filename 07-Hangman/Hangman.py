import random

MyWords = ["sajjad","programmer","computer","phone","mobile","mouse","laptop","keyboard","python","graphic","ram","cpu","hard"]

randomWord = random.choice(MyWords)

chance = len(randomWord)

print("Welcome to the Game !")

wordLetterList = ['-'] * chance

while chance >= 0:
    print("\nYour Choice Count = ",chance)
    for letter in wordLetterList:
        print(letter,end="")
    if chance == 0:
        print("\n😣 You Lose!")
        break
    if '-' not in wordLetterList:
        print("\n🥳 You Win !")
        break

    print("\nGuess the letter : ",end="")
    guess = input()
    if guess == "":
        print("Please Enter a letter ...")
    guess = guess.lower()
    if guess in randomWord :
        for i in range(len(randomWord)):
            if guess == randomWord[i]:
                wordLetterList[i] = guess
        print("✅")
    else:
        chance -= 1
        print("❌")

print("End The Game ..... Thank's For Play , Come Back Again !")


