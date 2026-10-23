import random

def main():
    level = pick_level()
    guess_number(level)


def pick_level():
    lvl = input("Enter a level ('easy'/'hard'): ")
    if lvl == "easy":
        return 10
    else:
        return 5
    

def guess_number(lives):
    number = random.randint(1, 100)
    while lives > 0:
        print(f"\nYou have {lives} lives")
        guess = int(input("Choose a number between 1 and 100: "))
        if guess == number:
            print(f"\nYou win!!! The number was {number}!")
            break
        elif guess < number:
            print("\nToo low!")
            lives -= 1
        else:
            print("\nToo high!")
            lives -= 1
    if lives == 0:
        print(f"\nYou lose! The number was {number}!")


if __name__ == "__main__":
    main()