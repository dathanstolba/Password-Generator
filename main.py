import random
import string

# Generates the random password
def generatePassword(length):

    # Includes all ascii letters(uppercase and lowercase), numbers, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return(password)

# Main function
def main():
    # Gets the length of password needed from the user
    length = int(input("What is the desired length of the password you want to generate? (INTEGERS ONLY):"))

    if length < 8:
        print("A strong password should be at least 8 characters.")
        return

    password = generatePassword(length)

    print(f"Here is your strong password: {password}")

# Checks if the script is run directly
if __name__ == "__main__":
    main()