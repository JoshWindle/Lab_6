alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"





def vigenere_sq():
    print("|   |", end="")

    for letter in alphabet:
        print(f" {letter} |", end="")

    print()
    print("|---|" + "---|" * 26)

    for i in range(26):
        print(f"| {alphabet[i]} |", end="")

        for j in range(26):
            index = (i + j) % 26
            print(f" {alphabet[index]} |", end="")

        print()




def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]
def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    cipher_index = (key_index + plaintext_index) % 26

    return index_to_letter(cipher_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = ""
    key_position = 0

    for letter in plaintext:
        if letter in alphabet:
            key_letter = key[key_position % len(key)]

            cipher_letter = vigenere_index(key_letter, letter, alphabet)
            ciphertext += cipher_letter

            key_position += 1
        else:
            ciphertext += letter

    return ciphertext


def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cypher_index = letter_to_index(cypher_letter, alphabet)

    plaintext_index = (cypher_index - key_index) % 26

    return index_to_letter(plaintext_index, alphabet)


def decrypt_vignere(key, cipher_text, alphabet):
    plaintext = ""
    key_position = 0

    for letter in cipher_text:
        if letter in alphabet:
            key_letter = key[key_position % len(key)]

            plaintext_letter = undo_vigenere_index(key_letter, letter, alphabet)
            plaintext += plaintext_letter

            key_position += 1
        else:
            plaintext += letter

    return plaintext


def main():
    while True:
        print("\nVigenere Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            key = input("Enter a keyword: ").upper()
            plaintext = input("Enter a message: ").upper()

            encrypted = encrypt_vigenere(key, plaintext, alphabet)
            print("Encrypted message:", encrypted)

        elif choice == "2":
            key = input("Enter a keyword: ").upper()
            cipher_text = input("Enter encrypted text: ").upper()

            decrypted = decrypt_vignere(key, cipher_text, alphabet)
            print("Decrypted message:", decrypted)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()