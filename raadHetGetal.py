
def raadHetGetal(userName):
    import random

    def endRound():
        while True:
            playAgain = input("Wil je nog een keer spelen? j/n").lower()
            if(playAgain == 'j'):
                startGame()
                break
            elif(playAgain == 'n'):
                return
            else:
                print('incorrect input, probeer opnieuw')


    def startGame():
        guessAmount = 0
        guess = ''
        randomNumber = random.randint(0, 10)


        while guessAmount < 3:
            guess = input("vul je gok in: ")

            try:
                if int(guess) == randomNumber:
                    print('gefeliciteerd je hebt gewonnen')
                    endRound()
                    break
                else:
                    print("Helaas dat klopt niet, probeer het nog een keer")
                    guessAmount += 1
            except ValueError:
                print("Ongeldige invoer, voer een getal in.")

        print("helaas je hebt geen pogingen meer, de computer heeft gewonnen!")
        endRound()

    wantsRules = input("Welkom bij raad het getal, " + userName + " wil je de spel regels? J/N").lower()

    while not wantsRules == "j" and not wantsRules == "n":
        wantsRules = input("Jouw vorige antwoord herkennen wij niet vul alstublieft nog een keer in, wil je de regels? J/N").lower()



    if(wantsRules == 'j'):
        print("\nHet doel van het spel is om een getal tussen de 0 en 10 te raden.\n"
              "De computer kiest willekeurig een getal, en jij krijgt 3 pogingen om het juiste getal te raden.\n"
              "Raad je het getal binnen 3 pogingen, dan win je! Anders wint de computer.\n"
              "Druk op Enter om verder te gaan.")
        input()
        startGame()
    else:
        startGame()

