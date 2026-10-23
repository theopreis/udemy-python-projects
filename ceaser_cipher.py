import string


def main():
    opt = ""
    while opt != "no":
        mode = input("Do you want to encrypt or decrypt? ('encrypt'/'decrypt'): ")
        if mode != "encrypt" and mode != "decrypt":
            raise ValueError("Invalid option")
        else:
            ceaser_cipher(mode)
        opt = input("Do you want to continue? ('yes'/'no'): ")
        if opt != "yes" and opt != "no":
            raise ValueError("Invalid option")


def ceaser_cipher(mode):
    new_text = []
    if mode == "encrypt":
        text = input("Enter message to be encrypted: ").strip().lower()
        try:
            shift = int(input("Enter shift: "))
        except ValueError:
            raise ValueError("Shift must be an integer")
        if not text.isalpha() and " " not in text:
            raise ValueError("Enter only letters")
        if shift > 25 or shift < 0:
            raise ValueError("Invalid shift")
        for letter in text:
            i = 0
            if letter != " ":
                for match in string.ascii_lowercase:
                    if letter == match:
                        new_letter = (string.ascii_lowercase + string.ascii_lowercase)[i + shift]
                    i += 1
                new_text.append(new_letter)
            else:
                new_text.append(letter)
    else:
        text = input("Enter message to be decrypted: ").strip().lower()
        try:
            shift = int(input("Enter shift: "))
        except ValueError:
            raise ValueError("Shift must be an integer")
        if not text.isalpha() and " " not in text:
            raise ValueError("Enter only letters")
        if shift > 25 or shift < 0:
            raise ValueError("Invalid shift")
        for letter in text:
            i = 0
            if letter != " ":
                for match in string.ascii_lowercase:
                    if letter == match:
                        new_letter = (string.ascii_lowercase + string.ascii_lowercase)[i + 26 - shift]
                    i += 1
                new_text.append(new_letter)
            else:
                new_text.append(letter)
    print(f"The {mode}ed text is: {"".join(new_text)}")


if __name__ == "__main__":
    main()