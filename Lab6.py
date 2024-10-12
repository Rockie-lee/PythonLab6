def vigenere_sq(alphabet):

    print("|   | " + " | ".join(alphabet) + " |")
    print("|---|" + "---|" * len(alphabet))

    for i in range(len(alphabet)):
        row = alphabet[i] + " | "
        for j in range(len(alphabet)):
            row += alphabet[(i + j) % len(alphabet)] + " | "
        print(row)


def letter_to_index(letter, alphabet):

    if letter in alphabet:
        return alphabet.index(letter)
    else:
        return -1


def index_to_letter(index, alphabet):

    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''


def vigenere_index(key_letter, plaintext_letter, alphabet):

    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    if key_index != -1 and plaintext_index != -1:
        return index_to_letter((plaintext_index + key_index) % len(alphabet), alphabet)
    return ''

def encrypt_vigenere(key, plaintext, alphabet):
    key_length = len(key)
    key_index = 0
    ciphertext = ""

    for letter in plaintext:

        upper_letter = letter.upper()

        if upper_letter in alphabet:
            key_letter = key[key_index % key_length].upper()

            ciphertext_letter = vigenere_index(key_letter, upper_letter, alphabet)
            ciphertext += ciphertext_letter

            key_index += 1
        else:

            ciphertext += letter

    return ciphertext

def undo_vigenere_index(key_letter, cypher_letter, alphabet):

    key_index = letter_to_index(key_letter, alphabet)
    cypher_index = letter_to_index(cypher_letter, alphabet)

    if key_index != -1 and cypher_index != -1:
        return index_to_letter((cypher_index - key_index) % len(alphabet), alphabet)
    return ''

def decrypt_vigenere(key, cipher_text, alphabet):
    key_length = len(key)
    key_index = 0
    plaintext = ""

    for letter in cipher_text:

        upper_letter = letter.upper()

        if upper_letter in alphabet:
            key_letter = key[key_index % key_length].upper()

            plaintext_letter = undo_vigenere_index(key_letter, upper_letter, alphabet)
            plaintext += plaintext_letter

            key_index += 1
        else:
            plaintext += letter

    return plaintext

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("Vigenère Square:")
    vigenere_sq(alphabet)

    while True:
        choice = input("Choose an action: 1) Encrypt 2) Decrypt 3) Exit: ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            encrypted_text = encrypt_vigenere(key, plaintext, alphabet)
            print(f"Encrypted text: {encrypted_text}")

        elif choice == '2':
            cipher_text = input("Enter the ciphertext: ")
            key = input("Enter the key: ")
            decrypted_text = decrypt_vigenere(key, cipher_text, alphabet)
            print(f"Decrypted text: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
