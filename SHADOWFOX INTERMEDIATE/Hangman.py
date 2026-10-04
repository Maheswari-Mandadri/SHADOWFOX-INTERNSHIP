#2. Hangman: Implement the wordguessing game with visual progress and hints.
import random

words = ["python", "computer", "programming", "developer", "machine"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_guesses:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    if "_" not in display:
        print("Output: Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    if wrong_guesses == 1:
        print("Hint: The word is related to computers.")

    if wrong_guesses == 2:
        print("Hint: The word has", len(word), "letters.")

else:
    print("\nOutput: Game Over!")
    print("The word was:", word)