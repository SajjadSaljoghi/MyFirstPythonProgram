from pyfiglet import figlet_format
from operator import itemgetter
from colorama import Fore
import random
import os
import time

gameBoared = []
#----------------------------------------------
#Functions
#----------------------------------------------
def ShowGameBoared():
    for i in range(len(gameBoared)):
        for j in range(len(gameBoared)):
            if gameBoared[i][j] == "X":
                print(Fore.RED + f"{gameBoared[i][j]} ",end="")
            elif gameBoared[i][j] == "O":
                print(Fore.GREEN + f"{gameBoared[i][j]} ",end="")
            else:
                print(Fore.RESET + f"{gameBoared[i][j]} ",end="")
        print("\n")

#----------------------------------------------
def FillGameBoared():
    for i in range(3):
        gameBoared.append(['-','-','-'])

#----------------------------------------------
def CheckFillGameBoared():
    if '-' in gameBoared[0] or '-' in gameBoared[1] or '-' in gameBoared[2]:
        return False
    else:
        return True

#----------------------------------------------
def InsertToGameBoared(row ,column ,player):
    if row >= len(gameBoared) or column >= len(gameBoared):
        print(f"Your Row Or Column must be between 0 to {len(gameBoared)-1}")
        time.sleep(3)
        return False
    for i in range(len(gameBoared)):
        for j in range(len(gameBoared)):
            if i == row and j == column:
                if player == "player1":
                    if gameBoared[i][j] != '-':
                        print("This is Fill... Please select another")
                        time.sleep(3)
                        return False
                    else:
                        gameBoared[i][j] = "X"
                        return True
                else:
                    if gameBoared[i][j] != '-':
                        if player == "CPU":
                            return False
                        else:
                            print("This is Fill... Please select another")
                            time.sleep(3)
                        return False
                    else:
                        gameBoared[i][j] = "O"
                        return True

#----------------------------------------------
def ShowTheGame(player):
    while True:
        os.system("cls")
        ShowGameBoared()
        print(Fore.RESET)
        if Check_Game() == "continue":
            if player=="CPU":
                player_row = random.randint(0,2)
                player_column = random.randint(0,2)
            else:
                print(f"{player} :")
                player_row = int(input("Please Enter a row = "))
                player_column = int(input("Please Enter a column = "))
            flag = InsertToGameBoared(player_row ,player_column ,player)
            if flag:
                break
            else:
                continue
        else:
            break

#----------------------------------------------
def ContinueTheGame(player):
    if Check_Game() != "continue":
        os.system("cls")
        ShowGameBoared()
        print(Fore.RESET)
        if Check_Game()=="Draw":
            print("Draw!!!! See You Later Again......")
        else:
            print(player)
            if player == "CPU":
                print("Winner is CPU")
            elif player == "player2":
                print("Winner is player2")
            else:
                print("Winner is player1")
        return False
    else:
        return True

#----------------------------------------------
def Check_Game():
    if gameBoared[0]==['X','X','X'] or gameBoared[1]==['X','X','X'] or gameBoared[2]==['X','X','X']:
        return "X"
    elif list(map(itemgetter(0), gameBoared))==['X','X','X'] or list(map(itemgetter(1), gameBoared))==['X','X','X'] or list(map(itemgetter(2), gameBoared))==['X','X','X']:
        return "X"
    elif (gameBoared[0][0]=='X' and gameBoared[1][1]=='X' and gameBoared[2][2]=='X') or (gameBoared[0][2]=='X' and gameBoared[1][1]=='X' and gameBoared[2][0]=='X'):
        return "X"
    elif gameBoared[0]==['O','O','O'] or gameBoared[1]==['O','O','O'] or gameBoared[2]==['O','O','O']:
        return "O"
    elif list(map(itemgetter(0), gameBoared))==['O','O','O'] or list(map(itemgetter(1), gameBoared))==['O','O','O'] or list(map(itemgetter(2), gameBoared))==['O','O','O']:
        return "O"
    elif (gameBoared[0][0]=='O' and gameBoared[1][1]=='O' and gameBoared[2][2]=='O') or (gameBoared[0][2]=='O' and gameBoared[1][1]=='O' and gameBoared[2][0]=='O'):
        return "O"
    elif CheckFillGameBoared():
        return "Draw"
    else:
        return "continue"

#------------------------------------------------
def Games_Mode(mode):
    if mode=="p": #Player Vs Player
        return "player2"
    elif mode=="c": #Player Vs CPU
        return "CPU"

#--------------------Main------------------------
print(figlet_format("TIC TAC TOE", font="bell"))
time.sleep(3)
print("Please Enter Game Mode : p 👉 Vs Player / c 👉 Vs CPU")
user_gameMode = input()
gameMode = Games_Mode(user_gameMode)
FillGameBoared()
startTime = time.time()
while True:
    if ContinueTheGame('player1')==True:
        ShowTheGame('player1')
    if ContinueTheGame('player1')==False:
        endTime = time.time()
        print(f"Elapsed Time : {endTime - startTime} Seconds")
        break
    if ContinueTheGame(gameMode)==True:
        ShowTheGame(gameMode)
    if ContinueTheGame(gameMode)==False:
        endTime = time.time()
        print(f"Elapsed Time : {endTime - startTime} Seconds")
        break



