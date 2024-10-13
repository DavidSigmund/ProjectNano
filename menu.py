from raadHetGetal import raadHetGetal
from galgje import galgje
from blackJack import blackJack
from snake import snakeGame
from enterTheDungeon.game_play import startEnterTheDugeon

def startProgram():
    print("Welkom in David's Nano project")
    print("""
    ______  ___ ______ _____ 
    |  _  \/ _ \|  _  \  _  |
    | | | / /_\ \ | | | | | |
    | | | |  _  | | | | | | |
    | |/ /| | | | |/ /\ \_/ /
    |___/ \_| |_/___/  \___/                 
    """)
    userName = getUser()

    colorCode = getThema()
    print(colorCode)

    menu(userName)


def menu(userName):
    menuKeuzen = input("Welke van de projecten wilt u bekijken/spelen \n"
                   "\n"
                   "  1. Raad het getal\n"
                   "  2. Galgje\n"
                   "  3. BlackJack\n"
                   "  4. Snake\n"
                   "  5. Enter the dungeon\n"
                   "\n")
    if (menuKeuzen == "1"):
        raadHetGetal(userName)
    elif (menuKeuzen == "2"):
        galgje(userName)
    elif (menuKeuzen == "3"):
        blackJack()
    elif (menuKeuzen == "4"):
        snakeGame()
    elif (menuKeuzen == "5"):
        startEnterTheDugeon(userName)
    else:
        print("deze keuzen bestaat niet probeer nog een keer")
        menu(userName)

def getThema():
    while True:
        themeColor = input("kies een thema kleur rood/groen/blauw/geel/wit: ")
        if(themeColor == "rood"):
            return '\033[31m'
        elif(themeColor == "blauw"):
            return '\033[34m'
        elif (themeColor == "geel"):
            return '\033[33m'
        elif (themeColor == "groen"):
            return '\033[32m'
        elif (themeColor == "wit"):
            return '\033[97m'
        else:
            print("deze keuzen bestaat niet")


def getUser():
    global userName
    userName = input("Vul je naam in: ")
    return userName


startProgram()
