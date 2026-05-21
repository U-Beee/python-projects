# ============================================================
# HANGMAN
# A word-guessing game played in the terminal.
# The program picks a secret word. The player guesses one
# letter at a time. Too many wrong guesses and they lose!
# ============================================================

import random  # We use this to pick a random word

# This is our list of words the game can choose from
word_list = ["python", "programming", "computer", "science", "keyboard",
             "software", "hangman", "algorithm", "function", "variable"]

# This list draws the hangman step by step as the player makes wrong guesses
hangman_art = [
    # 0 wrong guesses - empty gallows
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    # 1 wrong guess - head
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 2 wrong guesses - head and body
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 3 wrong guesses - head, body, one arm
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 wrong guesses - head, body, two arms
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    # 5 wrong guesses - head, body, arms, one leg
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    # 6 wrong guesses - full hangman, player loses
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

def play_hangman():
    # Pick a random word from the word list
    secret_word = random.choice(word_list)

    # Create a list of underscores, one for each letter in the secret word
    # For example, "python" becomes ["_", "_", "_", "_", "_", "_"]
    guessed_letters = ["_"] * len(secret_word)

    # This list keeps track of all letters the player has already guessed
    wrong_guesses = []

    # The player gets 6 wrong guesses before losing (matching the hangman art)
    max_wrong = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")

    # The game loop continues until the player wins or loses
    while True:
        # Show the current hangman drawing based on how many wrong guesses
        print(hangman_art[len(wrong_guesses)])

        # Show the word as underscores and correctly guessed letters
        # " ".join() puts a space between each element of the list
        print("Word: " + " ".join(guessed_letters))

        # Show which wrong letters have already been guessed
        print("Wrong guesses: " + ", ".join(wrong_guesses))
        print("Wrong guesses left: " + str(max_wrong - len(wrong_guesses)))

        # Check if the player has guessed all the letters (no underscores left)
        if "_" not in guessed_letters:
            print("\nYou won! The word was: " + secret_word)
            break  # Exit the loop

        # Check if the player has run out of guesses
        if len(wrong_guesses) >= max_wrong:
            print("\nYou lost! The word was: " + secret_word)
            break  # Exit the loop

        # Ask the player to guess a letter
        print("Guess a letter: ", end="")
        guess = input().lower()  # .lower() converts to lowercase so "A" and "a" are the same

        # Make sure the player entered exactly one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue  # Go back to the top of the loop

        # Check if the player already guessed this letter
        if guess in wrong_guesses or guess in guessed_letters:
            print("You already guessed that letter!")
            continue  # Go back to the top of the loop

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print("Correct!")
            # Reveal all positions in the word where this letter appears
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_letters[i] = guess  # Replace underscore with the letter
        else:
            # The letter is not in the word, add it to wrong guesses
            print("Wrong!")
            wrong_guesses.append(guess)

# Start the game
play_hangman()
