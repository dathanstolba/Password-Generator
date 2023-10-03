import random
import string
import tkinter as tk
import pyperclip

# Generates the random password
def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to handle the password generation button click
def generate_password():
    length = int(length_entry.get())

    if length < 8:
        result_label.config(text="A strong password should be at least 8 characters.")
        return

    password = generatePassword(length)
    result_label.config(text=f"Here is your strong password: {password}")
    generated_password.set(password)  # Set the generated password in a tkinter variable

# Function to handle the copy button click
def copy_password():
    password = generated_password.get()
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place a label and entry for password length
length_label = tk.Label(root, text="Enter length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Create a label to display the generated password
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create a tkinter variable to store the generated password
generated_password = tk.StringVar()

# Create a button to copy the password
copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI application
root.mainloop()
