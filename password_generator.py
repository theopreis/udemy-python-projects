import random
import string


def main():
    print("Welcome to password generator")
    max_password_lenth = len(string.ascii_lowercase) + len(string.ascii_uppercase) + len(string.digits) + len(string.punctuation)
    while True:
        lenth = int(input("What's the desired password lenth? "))
        if 8 <= lenth <= max_password_lenth:
            break
        elif lenth < 8:
            print("Password lenth must be at least 8 characters")
        else:
            print(f"Maximum password lenth is {max_password_lenth} characters")
            
    password = get_password(lenth)
    print(f"Your new password is {password}")
    save_password(password)


def get_password(l):
    chars = []
    types = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    chars.append(random.choice(string.ascii_lowercase))
    chars.append(random.choice(string.ascii_uppercase))
    chars.append(random.choice(string.digits))
    chars.append(random.choice(string.punctuation))

    for _ in range(l-4):
        while True:
            opt2 = random.choice(types)
            new_char = random.choice(opt2)
            if new_char not in chars:
                chars.append(new_char)
                break

    random.shuffle(chars)
    return "".join(chars)


def save_password(p): # maybe add error-handling code
    while True:
        opt = input("Would you like to save this password in a file? (y/n): ").lower().strip()
        if opt == "y":
            while True:
                purpose_opt = input("Would you like to add a tag to your password? (ex: password - purpose/service) (y/n): ")
                if purpose_opt == "y":
                    purpose = input("Enter tag: ")
                    saved_password = f"{p} - {purpose}"
                    break
                elif purpose_opt == "n":
                    saved_password = p
                    break
                else:
                    print("Invalid option")
            with open("generated_passwords.txt", "a") as file:
                file.write(f"{saved_password}\n")
            print("New password saved in 'generated_passwords.txt'")
            break
        elif opt == "n":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()