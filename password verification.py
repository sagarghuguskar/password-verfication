import tkinter as tk
from tkinter import messagebox

def validate_password(password):
    # Check if the password contains at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one symbol
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

def submit_form():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not password or not confirm_password:
        tk.messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        tk.messagebox.showerror("Error", "Passwords do not match!")
    elif not validate_password(password):
        tk.messagebox.showerror("Error", "Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one symbol (!@#$%^&*()_+)")
    else:
        correct_password_label.config(text="Correct password ✅ ")

# Create the tkinter window
root = tk.Tk()
root.title("Password Verification")

# Create the username label and entry widget
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the password label and entry widget
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the confirm password label and entry widget
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Create the label to display the correct password
correct_password_label = tk.Label(root, text="")
correct_password_label.pack()

# Start the tkinter event loop
root.mainloop()
