def main():
    opt = ""
    bids = {}
    while opt != "no":
        name = input("Enter your name: ")
        bids[name] = input("Enter your bid: $")
        opt = input("Will anyone else make a bid? (yes/no): ")
        print("\n" * 100)
    find_highest_bid(bids)

    
def find_highest_bid(dict):
    current_highest = {}
    highest_bid = -1
    for name in dict:
        if int(dict[name]) > highest_bid:
            highest_bid = int(dict[name])
            current_highest = {"name": name, "bid": highest_bid}
    print(f"The winner is {current_highest["name"]}, with a bid of ${current_highest["bid"]}")


if __name__ == "__main__":
    main()