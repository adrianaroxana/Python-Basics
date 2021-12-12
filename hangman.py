import random
import sys


def pick_capital():
    CAPITALS = [
        "Ankara",
        "Skopjie",
        "London",
        "Rome",
        "Moscow",
        "Bucharest",
        "Berlin",
        "Madrid",
        "Amsterdam",
        "Bruxelles",
        "Paris",
    ]
    return random.choice(CAPITALS)


def get_hashed(password):
    hashed_password = ["_"] * len(password)
    return hashed_password


def uncover(hashed_password, password, letter):
    for i in range(len(password)):
        if password[i].upper() == letter.upper():
            hashed_password[i] = password[i].upper()
    print(join_array(hashed_password, " "))


def update(password, hashed_password, used_letters, letter):
    if not (letter.isalpha()):
        print("Only letters allowed")
    elif len(letter) == 1:
        if letter not in used_letters:
            if letter in password.upper():
                uncover(hashed_password, password, letter)
            else:
                global life_points
                life_points -= 1
                print("The word does not contain letter " + letter)
                print(f"Number of tries remaining : {life_points}")

            used_letters.append(letter)
        else:
            print("The letter was tried before!")
    else:

        if is_win(letter, password):
            print("You guessed the word")
            print("The word was " + str(password.upper()))
            print("Thanks, you saved me! You win!")
            again = str(input("Do you want to play again (type yes or no): "))
            if again == "yes":
                new_game()
            else:
                sys.exit()
        else:
            life_points -= 1
    print("Already used letters: ", used_letters)
    print("............................................................")


def is_win(hashed_password, password):
    return join_array(hashed_password, "") == password.upper()


def is_loose():
    return life_points == 0


def get_input():
    guess = input("Please guess a letter: ")
    return guess.upper()


def play_hangman(password, hashed_password, used_letters):
    while life_points > 0:
        letter = get_input()
        # update word found
        # check if word is found
        update(password, hashed_password, used_letters, letter)
        if is_win(hashed_password, password):
            print("Thanks, you saved me! You win!")
            print("The word was " + str(password.upper()))
            again = str(input("Do you want to play again (type yes or no): "))
            if again == "yes":
                new_game()
            else:
                sys.exit()
        if is_loose():
            print("Game Over!")
            print("~~~~~~~~~~~")
            print("|  / |")
            print("| / (_)")
            print("|   /|\ ")
            print("|    |")
            print("|   / \ ")
            print("|")
            print("|__")
            print(
                "HANGMAN Thanks, you killed me... The correct word was: "
                + str(password.upper())
            )

            again = str(input("Do you want to play again (type yes or no): "))
            if again == "yes":
                new_game()
            else:
                sys.exit()


def new_game():
    global life_points
    life_points = 5
    name = input("What is your name? ")
    print("Hello, " + name, "Time to play hangman!")
    print("")
    print("Start guessing...")
    letters = []
    password = pick_capital()
    hashed_password = get_hashed(password)
    print(join_array(hashed_password, " "))
    play_hangman(password, hashed_password, letters)


def join_array(array, char):
    return char.join(array)


def main():
    new_game()


if __name__ == "__main__":
    main()
