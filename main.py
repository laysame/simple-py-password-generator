# Password Generator Project
import random


def start_generator():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    return nr_letters, nr_symbols, nr_numbers


def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for _ in range(nr_letters):
        random_letters = random.choice(letters)
        password.append(random_letters)
    for _ in range(nr_symbols):
        random_symbols = random.choice(symbols)
        password.append(random_symbols)
    for _ in range(nr_numbers):
        random_numbers = random.choice(numbers)
        password.append(random_numbers)

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters into a string
    password_str = ''.join(password)

    return password_str


if __name__ == "__main__":
    # Calling start_generator to get parameters
    params = start_generator()
    password = generate_password(*params)
    print(f"Your password is: {password}")
