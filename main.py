from random import choice

print("""
* Let's Play Hangman!
* Enter your name to start.
* Choose a letter, or guess the word.
""")

def run_game():
    # populate the list with words
    word: str = choice(["apple", "secret", "banana", "python", "postgresql", "grapes"])

    username: str = input("What you your name? >> ")
    print(f"Welcome to hangman {username.title()}")

    guessed: str = ""
    tries: int = 3 # set the number of tries

    while tries > 0:
        blanks: int = 0

        print("Word: ", end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print("_", end="")
                blanks += 1

        print()  # Adds a blank line

        if blanks == 0:
            print("You got it!")
            break

        prompt: str = input("Guess the word? (y)es / (n)o: ").lower()
        if prompt == "y":
            if input("What is the word? : ").lower() == word.lower():
                print(f"You guessed right! The word is '{word}'.")
                break
            else:
                print("You guessed wrong!")

        guess: str = input("Enter a letter: ").lower()

        if len(guess) > 1:
            print("You can only guess one letter at a time.")
            continue

        if guess in guessed:
            print(f"You already used: '{guess}'. Please try with another letter!")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... {tries} remaining.")

            if tries == 0:
                print(f"No more tries remaining... The word was '{word}'You lose.")
                break


if __name__ == "__main__":
    run_game()
