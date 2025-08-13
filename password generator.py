import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + numbers + symbols

    if not all_chars:
        return "Error: No character sets selected!"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔑 Password Generator 🔑")
    
    length = int(input("Enter password length (default 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    generated_password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"\nGenerated Password: {generated_password}")
