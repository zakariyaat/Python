import random
import string

def generate_password(length=12):
    """Generate a random secure password."""
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n--- Random Password Generator ---")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
