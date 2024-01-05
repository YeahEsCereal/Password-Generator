import random
import colorama
import string

if __name__ == "__main__":
    # Print title
    print('Password Generator')
    print('------------------')

# Generate the password
def randomPassword():
    passwordCharacters = []
    size = input('How long do you want your password? ')
    try:
        for i in range(int(size)):
            # If the character should be a number or letter
            numOrLet = random.randint(1, 2)
            if numOrLet == 1:
                # Add a random number to the characters
                passwordCharacters.append(str(random.randint(0, 9)))
            elif numOrLet == 2:
                # If the letter should be uppercase or lowercase
                upperOrLower = random.randint(1, 2)
                if upperOrLower == 1:
                    # Add a random lowercase letter to the characters
                    passwordCharacters.append(random.choice(string.ascii_lowercase))
                else:
                    # Add a random uppercase letter to the characters
                    passwordCharacters.append(random.choice(string.ascii_uppercase))
        # Join the characters and print it
        print(colorama.Fore.GREEN + "".join(passwordCharacters))
        print(colorama.Fore.RESET + '------------------')
        # Ask if you want to make another password
        again = input("Would you like to make another one? (y/n) ")
        if again.lower() == 'y':
            randomPassword()
        else:
            pass
    except ValueError:
        randomPassword()

if __name__ == "__main__":
    randomPassword()
