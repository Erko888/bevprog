import random

def main():
    randomSzam = random.randint(1, 100)
    yourGuess = int(input("your guess: "))
    numberOfGuesses = 0
    while randomSzam != yourGuess:
        if randomSzam > yourGuess:
            print("My number is larger")
            yourGuess = int(input("your guess: "))
        else:
            print("My number is smaller")
            yourGuess = int(input("your guess: "))
        numberOfGuesses += 1
    print("Thats my number!")
    print("Number of guesses: {0}" .format(numberOfGuesses+1))


if __name__ == "__main__":
    main()