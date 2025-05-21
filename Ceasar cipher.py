def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve case (uppercase/lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Non-alphabetic characters stay the same
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g. 3): "))

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")

if __name__ == "__main__":
    main()
