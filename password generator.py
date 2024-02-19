import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits 
    pwd = ''.join(random.choice(char) for _ in range(length))
    return pwd

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError as e:
        print("Invalid length. Length should be a positive integer")

    if length <= 0:
        print("Invalid password length. Please enter a positive integer.")
        return

    pwd = generate_password(length)
    print("Generated Password:", pwd)

if __name__ == "__main__":
    main()

