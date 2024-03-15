import user_management
import mines_game
import transactions

def main_menu():
    while True:
        print("Welcome to PhilMoney Casino Suite!")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter phone/email: ")
            password = input("Enter password: ")
            if user_management.register_user(username, password):
                game_menu(username)  # Go to the game menu after registration
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            transactions.update_balance(username, amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if transactions.update_balance(username, -amount):
                print("Withdrawal successful.")
        elif choice == '4':
            balance = transactions.get_balance(username)
            print(f"Your current balance is: {balance}")
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("Welcome to PhilMoney Casino Suite!")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter phone/email: ")
            password = input("Enter password: ")
            user_management.register_user(username, password)
        elif choice == '2':
            username = input("Enter phone/email: ")
            password = input("Enter password: ")
            if user_management.login_user(username, password):
                game_menu(username)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()