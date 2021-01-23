def save_to_file(email, password):
    with open("passwords.txt", "a+") as file:
        file.write(email + " " + password + "\n")


def read(number):
    with open("passwords.txt","r") as file:
        passwords = file.readlines()

    return passwords[number]


