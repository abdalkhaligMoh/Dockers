import random
import string

def generate_password():
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Generate Random Characters
    password_characters = [random.choice(uppercase_letters),
                           random.choice(lowercase_letters),
                           random.choice(digits),
                           random.choice(special_characters)]
    
    # Fill remaining characters
    remaining_length = 8 - len(password_characters)
    
    for _ in range(remaining_length):
        password_characters.append(random.choice(uppercase_letters + lowercase_letters + digits + special_characters))

    # shuffle password
    random.shuffle(password_characters)

    password = ''.join(password_characters)
    return password

print(generate_password())
