from rich import print
from random import choice
import os

WORD_LIST = ["summer", "hack"]

def clear_screen():
    if os.name == 'nt': # windows
        _ = os.system('cls')
    else: # macOS and linux
        _ = os.system('clear')

def game():
    word = choice(WORD_LIST)
    guesses = 0
    print(f"[b]The word is {len(word)} letters long.[/b]")
    while guesses < 10:
        guess = input("Guess: ").lower().strip()
        if guess == word:
            print("[green]You Win![/green]")
            quit(0)
        else:
            print("Wrong.")
            guesses += 1
            print(f"You have {10 - guesses} guesses remaining.")
            clear_screen()

def main():
    clear_screen()
    print("Welcome to hangman! Guess the word in less than 10 guesses or [red]you'll perish[/red]")
    game()


if __name__ == "__main__":
    main()
