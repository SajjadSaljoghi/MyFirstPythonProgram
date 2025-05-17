import random
randomNumber = random.randint(1,200)
print("Hello , I Have a number . Let's Play The Game To Guess My Number and win😉")
attempts = 1
while True:
    print("What's Your Guess?🤔")
    guessNumber = int(input())
    if guessNumber == randomNumber:
        print("Congratulations! 😍🥳 You win and I Lose😥, another Time You'll see how i win ...")
        print("Your Attempts = ",attempts)
        break
    elif guessNumber < randomNumber:
        print("Try Again! too low , Go up 🔼")
        attempts = attempts + 1
    else:
        print("Try Again! too high , Go down 🔽")
        attempts = attempts + 1



        