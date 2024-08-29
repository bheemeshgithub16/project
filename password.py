import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    """Generate a random password with the given complexity"""
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    """Get user preferences for the password"""
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(e)

    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    return length, include_uppercase, include_numbers, include_special

def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_numbers, include_special = get_user_preferences()
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

