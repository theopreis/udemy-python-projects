COFFEES = {
    "espresso": {"Price": 1.5,"Water": 50, "Coffee": 18},
    "latte": {"Price": 2.5, "Water": 200, "Coffee": 24, "Milk": 150},
    "cappuccino": {"Price": 3, "Water": 250, "Coffee": 24, "Milk": 100},
}
COINS = {"penny": 0.01, "nickle": 0.05, "dime": 0.1, "quarter": 0.25}


def main():
    resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Money": 0}
    opt = ""
    while opt != "off":
        opt = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        if opt == "report":
            report(resources)
        elif opt != "off":
            if check_ingredients(opt, resources):
                resources = subtract_ingredients(opt, resources)
                if check_money(opt):
                    resources["Money"] += COFFEES[opt]["Price"]
                    print(f"\nEnjoy your {opt}!☕")


def check_ingredients(coffee, ingredients):
    missing = []
    if coffee in COFFEES:
        for ingredient in COFFEES[coffee]:
            if ingredient in ingredients and ingredients[ingredient] < COFFEES[coffee][ingredient]:
                missing.append(ingredient)
        if missing:
            print("The following ingredients are missing:")
            for ingredient in missing:
                print("-", ingredient, sep="")
            return False
        else:
            return True
    else:
        print("Not an available coffee, try again")
        return False


def subtract_ingredients(coffee, ingredients):
    for ingredient in COFFEES[coffee]:
        if ingredient in ingredients:
            ingredients[ingredient] -= COFFEES[coffee][ingredient]
    return ingredients


def check_money(coffee):
    coin_amounts = {"penny": 0, "nickle": 0, "dime": 0, "quarter": 0}
    total = 0
    print("\nPlease insert coins.")
    for coin in coin_amounts:
        coin_amounts[coin] = int(input(f"Enter {coin} amount: "))
        total += coin_amounts[coin] * COINS[coin]
    if total < COFFEES[coffee]["Price"]:
        print("\nSorry, that's not enough money. Money refunded.")
        return False
    else:
        if total > COFFEES[coffee]["Price"]:
            print(f"Here is ${round(total - COFFEES[coffee]["Price"], 2)} in change")
        return True


def report(resource_dict):
    print(
        f"Water: {resource_dict['Water']}ml",
        f"Milk: {resource_dict['Milk']}ml",
        f"Coffee: {resource_dict['Coffee']}g",
        f"Money: ${resource_dict['Money']}", sep="\n"
    )


if __name__ == "__main__":
    main()