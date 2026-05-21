# ============================================================
# TYPING TEST
# A terminal program that tests how fast and accurately you type.
# A random sentence is shown. You type it out, and the program
# measures your speed (Words Per Minute) and accuracy (%).
# ============================================================

import time    # Used to measure how long the user takes to type
import random  # Used to pick a random sentence

# A list of sentences for the typing test
sentences = [
    "the quick brown fox jumps over the lazy dog",
    "python is a great programming language for beginners",
    "software engineers solve problems with code every day",
    "practice makes perfect when learning to type faster",
    "computers process information using binary code",
    "learning to code opens many doors in your career",
    "algorithms are step by step instructions to solve a problem",
    "a strong foundation in mathematics helps in programming"
]

def count_words(text):
    # Split the text into a list of words and count them
    # For example, "hello world" becomes ["hello", "world"] → 2 words
    words = text.split()
    return len(words)

def calculate_accuracy(original, typed):
    # Compare the original sentence to what the user typed, word by word.
    # This function returns a percentage showing how accurate they were.

    original_words = original.split()   # Break original into individual words
    typed_words = typed.split()         # Break the user's input into individual words

    # Count how many words match (at the same position)
    correct = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1   # This word was typed correctly

    # Calculate accuracy as a percentage
    # We use len(original_words) as the total so missing words count against you
    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 1)  # Round to 1 decimal place

def run_typing_test():
    print("=" * 50)
    print("         WELCOME TO THE TYPING TEST")
    print("=" * 50)
    print("Type the sentence below as fast and accurately as you can.")
    print("Press Enter when you are done.\n")

    # Pick a random sentence from the list
    sentence = random.choice(sentences)

    # Show the sentence to the user
    print(">>> " + sentence + "\n")

    # Ask if the user is ready before starting the timer
    input("Press Enter to start the timer...")

    # Record the start time (in seconds since a fixed point in the past)
    start_time = time.time()

    # Get the user's typed input
    typed = input("Type here: ")

    # Record the end time
    end_time = time.time()

    # Calculate how many seconds the user took
    elapsed_time = end_time - start_time

    # --- CALCULATE RESULTS ---

    # Words Per Minute (WPM): standard measure of typing speed
    # The formula is: (number of words typed / time in seconds) * 60
    words_typed = count_words(typed)
    wpm = (words_typed / elapsed_time) * 60
    wpm = round(wpm, 1)  # Round to 1 decimal place

    # Accuracy: percentage of words typed correctly
    accuracy = calculate_accuracy(sentence, typed)

    # --- DISPLAY RESULTS ---
    print("\n" + "=" * 50)
    print("              YOUR RESULTS")
    print("=" * 50)
    print("Time taken    : " + str(round(elapsed_time, 2)) + " seconds")
    print("Words typed   : " + str(words_typed))
    print("Speed         : " + str(wpm) + " WPM (words per minute)")
    print("Accuracy      : " + str(accuracy) + "%")

    # Give the user a rating based on their WPM score
    print("\nRating: ", end="")
    if wpm >= 60:
        print("Excellent! You are a very fast typist!")
    elif wpm >= 40:
        print("Good job! You have a solid typing speed.")
    elif wpm >= 20:
        print("Not bad! Keep practicing to get faster.")
    else:
        print("Keep it up! Regular practice will improve your speed.")

    # Show whether they were perfectly accurate or not
    if accuracy == 100:
        print("Perfect accuracy! Not a single mistake.")
    else:
        print("Tip: Focus on accuracy first, speed will follow.")

    print("=" * 50)

    # Ask if the user wants to try again
    print("\nWould you like to try again? (yes/no): ", end="")
    again = input().lower()
    if again == "yes" or again == "y":
        run_typing_test()   # Call the function again to restart
    else:
        print("\nThanks for practicing! See you next time.")

# Start the typing test
run_typing_test()
