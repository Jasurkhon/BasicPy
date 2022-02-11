master_password = input("What is the master password: ")

def add():
    name = input("Enter username: ")
    password = input("Enter password: ")
    with open("passwords.txt", "a") as f:
        f.write("username: " + name + " password: " + password + "\n")

def view():
    with open("passwords.txt", "r") as f:
        print(f.read().rstrip())

while True:
    option = input("Do you want to add new password or view existing one 'add' or 'view' or 'q' to exit: ").lower()
    if option == "add":
        add()
    elif option == "view":
        view()
    elif option == "q":
        break
    continue