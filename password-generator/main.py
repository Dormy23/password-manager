import random
import string
import argparse

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Genera una password casuale."""
    characters = string.ascii_lowercase  # Lettere minuscole
    if use_uppercase:
        characters += string.ascii_uppercase  # Lettere maiuscole
    if use_digits:
        characters += string.digits  # Numeri
    if use_special_chars:
        characters += string.punctuation  # Caratteri speciali

    # Genera la password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Password Generator - Crea password sicure.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Lunghezza della password (default: 12)")
    parser.add_argument("--no-uppercase", action="store_false", dest="use_uppercase", help="Escludi lettere maiuscole")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Escludi numeri")
    parser.add_argument("--no-special-chars", action="store_false", dest="use_special_chars", help="Escludi caratteri speciali")
    parser.add_argument("-n", "--number", type=int, default=1, help="Numero di password da generare (default: 1)")

    args = parser.parse_args()

    print("\nGenerazione password in corso...\n")
    for i in range(args.number):
        password = generate_password(
            length=args.length,
            use_uppercase=args.use_uppercase,
            use_digits=args.use_digits,
            use_special_chars=args.use_special_chars
        )
        print(f"Password {i + 1}: {password}")

    print("\nFatto! 🎉\n")

if __name__ == "__main__":
    main()