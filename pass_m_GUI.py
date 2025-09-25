import json
import random
import string
from tkinter import Tk, Label, Entry, Button, messagebox

# File to store passwords
PASSWORD_FILE = "passwords.json"

# Load existing passwords
def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save passwords to file
def save_passwords(data):
    with open(PASSWORD_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Check password strength
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        score += 1
    if not any(c.isspace() for c in password):
        score += 1

    if score == 5:
        return "Very Strong ✅"
    elif score >= 4:
        return "Strong 👍"
    elif score >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

# Generate random strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

# Save password
def save_password():
    site = entry_site.get().strip()
    user = entry_user.get().strip()
    pwd = entry_password.get().strip()

    if not site or not user or not pwd:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    passwords = load_passwords()
    passwords[site] = {"username": user, "password": pwd}
    save_passwords(passwords)
    messagebox.showinfo("Success", f"Password for {site} saved!")
    entry_site.delete(0, "end")
    entry_user.delete(0, "end")
    entry_password.delete(0, "end")

# Generate password button
def generate_and_fill():
    pwd = generate_password()
    entry_password.delete(0, "end")
    entry_password.insert(0, pwd)
    messagebox.showinfo("Password Generated", f"Generated Password: {pwd}\nStrength: {check_password_strength(pwd)}")

# GUI
root = Tk()
root.title("Password Manager")
root.geometry("400x300")

Label(root, text="Website:").pack(pady=5)
entry_site = Entry(root, width=40)
entry_site.pack()

Label(root, text="Username/Email:").pack(pady=5)
entry_user = Entry(root, width=40)
entry_user.pack()

Label(root, text="Password:").pack(pady=5)
entry_password = Entry(root, width=40)
entry_password.pack()

Button(root, text="Generate Password", command=generate_and_fill, bg="orange").pack(pady=5)
Button(root, text="Save Password", command=save_password, bg="green", fg="white").pack(pady=10)

root.mainloop()
