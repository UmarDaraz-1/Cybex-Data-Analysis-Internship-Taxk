import os

USERS_FILE = "users.txt"

def register(username, password):
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            pass  

    
    with open(USERS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:  
                continue
            stored_user, stored_pass = line.split(",")
            if stored_user == username:
                return " Username already exists!"

    
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")
    return " Registration successful!"


def login(username, password):
    if not os.path.exists(USERS_FILE):
        return " No users registered yet."

    with open(USERS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:  
                continue
            stored_user, stored_pass = line.split(",")
            if stored_user == username and stored_pass == password:
                return " Login successful!"
    return " Invalid username or password!"



while True:
    print("\n=== User Authentication System ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        print(register(user, pwd))

    elif choice == "2":
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        print(login(user, pwd))

    elif choice == "3":
        print(" Exiting... Goodbye!")
        break

    else:
        print(" Invalid choice, try again!")



