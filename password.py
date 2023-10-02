import secrets
import string


def generate_random_password(length=12):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_-+=<>?"

    # Combine the character sets into one if needed
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Use the secrets module to generate a secure random password
    password = ''.join(secrets.choice(all_characters) for _ in range(length))

    return password


# Usage example: generate a 16-character password
password = generate_random_password(16)
print(password)
