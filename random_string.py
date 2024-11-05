import random
import string

def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Set the desired password length
password_length = 12
password = generate_password(password_length)
print("Generated Password:", password)