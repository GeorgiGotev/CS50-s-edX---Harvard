def getGuess():
    n = 10
    playerGuess = input("What is your guess number: ")
    
    if n == float(playerGuess):
        print("You won!")
    else:
        print("You lose. Try again!")

getGuess()