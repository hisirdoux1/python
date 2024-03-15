# user_management.py

import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        print("Username already exists.")
        return False
    users[username] = {'password': password, 'balance': 1000}  # Starting balance for new accounts
    save_users(users)
    print("Registration successful!")
    return True

def login_user(username, password):
    users = load_users()
    user = users.get(username)
    if user and user['password'] == password:
        print("Login successful!")
        return True
    print("Invalid username or password.")
    return False
