import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Create a pool of characters to choose from
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Generated password:", password)