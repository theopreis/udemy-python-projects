import random


def main():
    opt = "y"
    while opt == "y":
        play_blackjack()
        opt = input("\n\nDo you want to play blackjack? (y/n): ")


def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    more_cards = "y"
    while more_cards == "y" and sum(your_cards) <= 21:
        print(f"\nYour cards are: {your_cards}\nYour total score is: {sum(your_cards)}")
        print(f"The computer's cards: {computer_cards}")
        more_cards = input("\nWould you like to get a new card? (y/n): ")
        if more_cards == "y":
            your_cards.append(random.choice(cards))
            if sum(your_cards) > 21 and 11 in your_cards:
                your_cards[your_cards.index(11)] = 1
    if sum(your_cards) > 21:
        print(f"\nYou lose! Your total score was: {sum(your_cards)}\nThe computer's total score was: {computer_cards[0]}")
        print(f"Your cards: {your_cards}. Computer cards: {computer_cards}")
    else:
        while sum(computer_cards) < sum(your_cards):
            computer_cards.append(random.choice(cards))
            if sum(computer_cards) > 21 and 11 in computer_cards:
                 computer_cards[computer_cards.index(11)] = 1
        if sum(computer_cards) > 21:
            print(f"\nYou win!!! Your total score was: {sum(your_cards)}\nThe computer's total score was: {sum(computer_cards)}")    
            print(f"Your cards: {your_cards}. Computer cards: {computer_cards}") 
        elif sum(computer_cards) == sum(your_cards):
            print(f"\nIt's a draw! Your total score was: {sum(your_cards)}\nThe computer's total score was: {sum(computer_cards)}")
            print(f"Your cards: {your_cards}. Computer cards: {computer_cards}")
        else:
            print(f"\nYou lose! Your total score was: {sum(your_cards)}\nThe computer's total score was: {sum(computer_cards)}")
            print(f"Your cards: {your_cards}. Computer cards: {computer_cards}")


if __name__ == "__main__":
    main()