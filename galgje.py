def galgje(userName):
    import random
    import json
    import datetime

    #credits naar chrishorton voor het galgje artwork https://gist.github.com/chrishorton
    from galgjeProgressionList import ProgressionList

    wordsFile = open("words.json", "r")
    jsonWordsData = json.load(wordsFile)

    def startGame():
        guessAmount = 0
        guessedLetters = []

        if(difficulty == "makkelijk"):
            word = random.choice(jsonWordsData["easy"])
        elif(difficulty == "normaal"):
            word = random.choice(jsonWordsData["normal"])
        else:
            word = random.choice(jsonWordsData["hard"])

        wordLength = len(word)

        def writeToPlayedList(newData):
            with open("playedList.json", 'r+') as file:
                fileData = json.load(file)
                fileData["played"].append(newData)
                file.seek(0)
                json.dump(fileData, file, indent=4)

        def printVersion():
            # scope van python is raar i guess
            nonlocal guessAmount
            guessVersion = ''

            if(guessedLetters[-1] in word):
                print(guessedLetters[-1] + ' zit erin')
            else:
                print(guessedLetters[-1] + ' zit er niet in')
                guessAmount += 1

            for letter in word:
                if(letter in guessedLetters):
                    guessVersion += letter
                else:
                    guessVersion += "_"

            print(guessVersion)

        # print het woord alleen voor de eerste keer
        print('_' * wordLength);


        # game loop
        while guessAmount < 9:
            print(ProgressionList[guessAmount])
            guess = input('Raad het woord of een letter: ')
            if(len(guess) > 1):
                if(word == guess):
                    print("Gefeliciteerd het woord was inderdaad: " + word + " je hebt gewonnen")
                    gameData = {"user": userName, "tries": guessAmount, "date": datetime.datetime.now().isoformat() , "result":"win"}
                    writeToPlayedList(gameData)
                    exit()
                else:
                    print("helaas dat klopt niet")
                    guessAmount += 1
            else:
                guessedLetters.append(guess)
                printVersion()

        print(ProgressionList[9])
        print("Helaas Je hangt :(")
        print("Het woord was " + word)
        gameData = {"user": userName, "tries": guessAmount, "date": datetime.datetime.now().isoformat()  , "result":"lose"}
        writeToPlayedList(gameData)
        exit()

    # dialog met de speler
    wantsRules = input("Welkom bij galgje, " + userName + " wil je de spel regels? Y/N").lower()
    while not wantsRules == "y" and not wantsRules == "n":
        wantsRules = input("ongeldige invoer , wil je de spel regels? Y/N").lower()

    if(wantsRules == 'y'):
        print("\nHet doel van het spel is om het woord te raden. Je vult een letter of een woord in als je een woord invukt probeer je het woord te raden en als je een letter invult kijk je of die er in zit")
        input()

    difficulty = input("Kies een moeilijkheidsgraad: makkelijk/normaal/moeilijk: ").lower()
    while not difficulty == "makkelijk" and not difficulty == "normaal" and not difficulty == "moeilijk":
        difficulty = input("ongeldige invoer, Kies een moeilijkheidsgraad: makkelijk/normaal/moeilijk: ").lower()

    startGame()

