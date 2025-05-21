print("Please Enter a Sentence to Print count of the word = ",end="")
userSentence = input()

wordList = userSentence.split(" ")
wordCount = 0

for word in wordList:
    if word != "":
        wordCount += 1


print("Count of Word = ",wordCount,end=" ")

     