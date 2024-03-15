# transactions.py

from user_management import load_users, save_users

def get_balance(username):
    users = load_users()
    return users.get(username, {}).get('balance', 0)

def update_balance(username, amount):
    users = load_users()
    user = users.get(username)
    if user:
        if amount < 0 and user['balance'] + amount < 0:
            print("Insufficient funds.")
            return False
        user['balance'] += amount
        save_users(users)
        print(f"Updated balance for {username}: {user['balance']}")
        return True
    print("User not found.")
    return False
