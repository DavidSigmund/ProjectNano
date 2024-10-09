import random

def blackJack():
    playerChips = 1000

    def placeBet(playerChips):
        while True:
            try:
                print(f"You have {playerChips} chips")
                betAmount = int(input("Fill amount in you want to bet: "))

                if betAmount > 0 and betAmount <= playerChips:
                    return betAmount
                else:
                    print(f"Not enough chips.")

            except ValueError:
                print("Incorrect input, please enter valid number.")


    def buildDeck():
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
        types = ["clover", "diamonds", "hearts", "spades"];
        deck = []
        for i in types:
            for j in values:
                deck.append(i + "-" + j)

        return deck

    def startRound(playerChips):
        if playerChips  <= 0:
            print("Game over.\nYou are all out of chips :(")
            exit()

        betAmount = placeBet(playerChips)

        # variables to see hand
        playerSum, playerAceCount = 0, 0
        dealerSum, dealerAceCount = 0, 0

        # build the deck
        deck = buildDeck()
        random.shuffle(deck)

        # deal cards
        dealerAceCount += checkAce(deck[0])
        dealerSum += getValue(deck.pop(0))

        for x in range(2):
            playerAceCount += checkAce(deck[0])
            playerSum += getValue(deck.pop(0))
            playerSum = reduceAce(playerSum, playerAceCount)

        print(f"Dealer has {dealerSum}")

        # game loop
        while playerSum < 21:
            playerSum = playerAction(deck, playerSum, dealerSum, playerAceCount, dealerAceCount, playerChips, betAmount)
        endRound(deck, playerSum, dealerSum, playerAceCount, dealerAceCount, playerChips, betAmount)


    def playerAction(deck, playerSum, dealerSum, playerAceCount, dealerAceCount, playerChips, betAmount):
        action = input(f"you have {playerSum} do you want to hit or stay? H/S").lower()
        while True:
            if action == "h":
                # hit
                return hit(playerSum, playerAceCount, deck)
            elif action == "s":
                # stand
                return endRound(deck, playerSum, dealerSum, playerAceCount, dealerAceCount, playerChips, betAmount)
            else:
                print("incorrect input")


    def endRound(deck, playerSum, dealerSum, playerAceCount, dealerAceCount, playerChips, betAmount):
        # give the dealer cards
        while dealerSum < 17:
            dealerAceCount += checkAce(deck[0])
            dealerSum += getValue(deck.pop(0))
            dealerSum = reduceAce(dealerSum, dealerAceCount)
            print(f"Dealer has: {dealerSum}")

        print(f"\nPlayer has: {playerSum}")

        # check outcome of round and calculate chips
        if playerSum > 21:
            print("Player busts! Dealer wins.")
            playerChips -= betAmount
        elif dealerSum > 21:
            print("Dealer busts! Player wins.")
            playerChips += betAmount
        elif playerSum > dealerSum:
            print("Player wins!")
            playerChips += betAmount
        elif playerSum < dealerSum:
            print("Dealer wins!")
            playerChips -= betAmount
        else:
            print("It's a tie!")

        print(f"chips: {playerChips}")
        input("press anything to play again..")
        startRound(playerChips)


    def hit(playerSum, playerAceCount, deck):
        playerAceCount += checkAce(deck[0])
        playerSum += getValue(deck.pop(0))
        playerSum = reduceAce(playerSum, playerAceCount)
        return playerSum


    def getValue(card):
        specialChars = ["A", "K", "J", "Q"]
        cardValue = card.split("-")

        if cardValue[1] in specialChars:
            if cardValue[1] == "A":
                return 11
            else:
                return 10
        else:
            return int(cardValue[1])

    def reduceAce(sum, aceCount):
        while sum > 21 and aceCount > 0:
            sum -= 10;
            aceCount -= 1;

        return sum;

    def checkAce(card):
        if card.split("-")[0] == "A":
            return 1

        return 0

    startRound(playerChips)

