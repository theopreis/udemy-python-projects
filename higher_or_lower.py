from celebrities import data
import random


def main():
    result = True
    while result == True:
        result = check_result(*play_game())


def play_game():
    celeb_1 = random.choice(data)
    celeb_2 = random.choice(data)
    if celeb_1['follower_count'] == celeb_2['follower_count']:
        while celeb_1['follower_count'] == celeb_2['follower_count']:
            celeb_2 = random.choice(data)
    print(f"Who has the highest follower count?\n\n1 - {celeb_1['name']}\n\n2 - {celeb_2['name']}")
    choice = input("\nType the number of your answer ('1'/'2'): ")
    return celeb_1['follower_count'], celeb_2['follower_count'], int(choice)


def check_result(n1, n2, ans):
    if n1 > n2:
        right_choice = 1
    else:
        right_choice = 2
    if ans == right_choice:
        print("\nCorrect!\n")
        return True
    else:
        print("\nWrong!\n")
        return False
    

if __name__ == "__main__":
    main()