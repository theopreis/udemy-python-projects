from hangman_list import word_list
import random
import string

def main():
    word = random.choice(word_list).upper()
    lives = get_level()
    dashes = []
    used_letters = []
    for letter in word:
        if letter == " ":
            dashes.append(" ")
        else:
            dashes.append("-")
    while lives > 0 and "".join(dashes) != word:
        letter_index = 0
        print("\nYou have", lives, "lives")
        print("You have used the letters:", ", ".join(used_letters))
        print("".join(dashes))
        while True:
            opt = input("Choose a letter: ").upper()
            if opt in string.ascii_uppercase:
                if opt in used_letters:
                    print("You have already used this letter, try another\n")
                else:
                    break
        used_letters.append(opt)
        if opt not in word:
            lives -= 1
        else:
            for letter in word:
                if opt == letter:
                    dashes[letter_index] = opt
                letter_index += 1
    if lives == 0:
        print(f"Better luck next time! The word was {word}!")
    else:
        print(f"Congrats, you got it right!!! The word was {word}!")


def get_level():
    while True:
        level = input("1 - Easy (20 lives)\n2 - Medium (10 lives)\n3 - Hard (5 lives)\nChoose level: ").lower()
        if level == "1" or level == "easy":
            return 20
        elif level == "2" or level == "medium":
            return 10
        elif level == "3" or level == "hard":
            return 5
        else:
            print("Invalid level: choose the number (1/2/3) or write the word (easy/medium/hard)")


if __name__ == "__main__":
    main()