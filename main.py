import os
from random import choice
from time import sleep
from hangmans import ASCII_ART
from rich import print

WORD_LIST = ["summer", "hack"]


def clear_screen():
    if os.name == "nt":  # windows
        _ = os.system("cls")
    else:  # macOS and linux
        _ = os.system("clear")


def game():
    word = choice(WORD_LIST)
    guesses = 0
    while guesses < 10:
        print(f"[b]The word is {len(word)} letters long.[/b]")
        print(f"You have {10 - guesses} guesses remaining.")
        guess = input("Guess: ").lower().strip()
        if guess == word:
            print("[green]You Win![/green]")
            print(f"The word was {word}")
            quit(0)
        else:
            print("Wrong.")
            guesses += 1
            print(f"[red]You have {10 - guesses} guesses remaining.[/red]")
            sleep(3)
            clear_screen()
        print(ASCII_ART[guesses-1])
    print(f"[red]You lost.[/red] The word was [b]{word}[/b]")


def main():
    clear_screen()
    print(
        "Welcome to hangman! Guess the word in less than 10 guesses or [red]you'll perish[/red]"
    )
    game()


if __name__ == "__main__":
    main()
