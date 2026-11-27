"""Word Guessing Game (PS 2B) - Python 3.

The computer picks a random word from a list and the player guesses it one
letter at a time. Correct letters are revealed; each wrong guess costs a life.

Run normally:        python word_guessing_game.py
Run in test mode:    python word_guessing_game.py --test   (secret word = PYTHON)
"""

import random
import sys

WORDS = ["PYTHON", "JAVA", "PROGRAM", "COMPUTER", "KEYBOARD", "FUNCTION",
         "VARIABLE", "ALGORITHM", "INTERNET", "DATABASE", "GAME"]
MAX_LIVES = 6
TEST_WORD = "PYTHON"          # fixed secret word used for testing


def pick_word(test_mode):
    """Return the secret word (fixed in test mode, random otherwise)."""
    return TEST_WORD if test_mode else random.choice(WORDS)


def show_word(secret, guessed):
    """Return the word with unguessed letters hidden, e.g. P _ _ _ _ _"""
    return " ".join(ch if ch in guessed else "_" for ch in secret)


def play_game(test_mode=False):
    secret = pick_word(test_mode)
    guessed = set()      # all letters tried
    wrong = []           # wrong letters, in order
    lives = MAX_LIVES

    print(f"\nI'm thinking of a {len(secret)}-letter word.")
    print(show_word(secret, guessed), f"  Lives left: {lives}")

    while lives > 0 and not all(ch in guessed for ch in secret):
        while True:
            text = input("Guess: ").strip()
            if len(text) == 1 and text.isalpha():
                letter = text.upper()
                break
            print(f"Invalid input. Enter a single letter. Lives left: {lives}")

        if letter in guessed:
            print(f"You already tried {letter}. No life lost. Lives left: {lives}")
            continue

        guessed.add(letter)
        if letter in secret:
            print("Correct!", show_word(secret, guessed), f"Lives left: {lives}")
        else:
            lives -= 1
            wrong.append(letter)
            print("Wrong!", show_word(secret, guessed), f"Lives left: {lives}")
            print("Wrong guesses:", ", ".join(wrong))

    if lives > 0:
        print(f"\nCongratulations! You guessed {secret}.")
    else:
        print(f"\nGame Over! The word was {secret}.")
        print("Better luck next time buddy")   
    print(f"Wrong guesses: {len(wrong)}")


def main():
    test_mode = "--test" in sys.argv
    print("=" * 36)
    print("       WORD GUESSING GAME")
    print("=" * 36)
    while True:
        play_game(test_mode)
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
