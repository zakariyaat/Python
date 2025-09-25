import re

def check_password_strength(password):
    # Initialize score
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    # Uppercase & lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    # Digits
    if re.search(r'\d', password):
        score += 1
    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    # No spaces
    if not re.search(r'\s', password):
        score += 1

    # Evaluate strength
    if score == 5:
        strength = "Very Strong ✅"
    elif score >= 4:
        strength = "Strong 👍"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Password Strength: {check_password_strength(pwd)}")
