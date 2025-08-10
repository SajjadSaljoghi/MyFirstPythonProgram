import os

def read_from_file():
    global database_words
    words = open("WordsList.txt",mode="r")
    
    wordsList = words.read().split("\n")

    database_words = []

    for i in range(0,len(wordsList),2):
        complete_word = {
            "en" : wordsList[i],
            "fa" : wordsList[i+1]
        }
        database_words.append(complete_word)

    words.close()
    


def show_menu():
    print("---------------------------------------------------")
    print("Welcome to My Translate App")
    print("1.Translate English To Finglish : ")
    print("2.Translate Finglish To English : ")
    print("3.Add Your Word To Database")
    print("4.clear System Console")
    print("5.Exit")

def Translate_to_finglish():
    print("Please Enter Your Sentence : ")
    user_words = input()
    user_words_list = user_words.split(" ")
    for user_word in user_words_list:
        for database_word in database_words:
            if user_word.lower() == database_word["en"].lower():
                print(database_word["fa"],end=" ")
                break
        else:
            print(user_word.lower(),end=" ")
    print()


def Translate_to_english():
    print("Please Enter Your Sentence : ")
    user_words = input()
    user_words_list = user_words.split(" ")
    for user_word in user_words_list:
        for database_word in database_words:
            if user_word.lower() == database_word["fa"].lower():
                print(database_word["en"],end=" ")
                break
        else:
            print(user_word.lower(),end=" ")
    print()

def Add_word_to_database():
    f = open("WordsList.txt",mode="a")

    print("Please Enter a Word that you want to save it! ... ")
    print("English Word = ")
    english = input()
    print("Finglish Word = ")
    finglish = input()

    f.write(f"\n{english}\n{finglish}")

    print("Your Word saved!")

    f.close()


while True:
    read_from_file()
    show_menu()
    user_choise = int(input())
    if user_choise == 1:
        Translate_to_finglish()
    elif user_choise == 2:
        Translate_to_english()
    elif user_choise == 3:
        Add_word_to_database()
    elif user_choise == 4:
        os.system("cls")
    elif user_choise == 5:
        exit()
    else:
        input("Please Enter a valid Number ...")