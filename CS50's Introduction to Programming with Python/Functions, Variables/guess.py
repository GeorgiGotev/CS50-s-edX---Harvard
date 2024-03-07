def getGuess():
    playerGuess = input("What is your guess number: ")
    return playerGuess
    


def main():
    guess=float(getGuess())

    if guess == 10:
        print("You won!")
    else:
        print("You lose. Try again!")


main()