import sys
import time

# Sample user data
users = {
    "1234": {
        "name": "Naveena",
        "balance": 1000.0,
        "transactions": []
    },
    "5678": {
        "name": "Alex",
        "balance": 500.0,
        "transactions": []
    }
}

def loading(message="Processing"):
    print(message, end='')
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()

def login():
    print("🔐 Welcome to Python ATM")
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin in users:
            print(f"\n✅ Login successful. Welcome, {users[pin]['name']}!\n")
            return pin
        else:
            attempts -= 1
            print(f"❌ Invalid PIN. Attempts left: {attempts}")
    print("🚫 Too many failed attempts. Exiting...")
    sys.exit()

def show_menu():
    print("""
========== ATM MENU ==========
1. View Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
==============================
""")

def view_balance(user):
    print(f"💰 Your current balance is: ₹{users[user]['balance']:.2f}")

def deposit(user):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            users[user]['balance'] += amount
            users[user]['transactions'].append(f"Deposited ₹{amount:.2f}")
            loading("Depositing")
            print("✅ Amount deposited successfully.")
        else:
            print("❌ Enter a valid amount.")
    except ValueError:
        print("❌ Invalid input.")

def withdraw(user):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Enter a valid amount.")
        elif amount > users[user]['balance']:
            print("❌ Insufficient balance.")
        else:
            users[user]['balance'] -= amount
            users[user]['transactions'].append(f"Withdrew ₹{amount:.2f}")
            loading("Withdrawing")
            print("✅ Please collect your cash.")
    except ValueError:
        print("❌ Invalid input.")

def transaction_history(user):
    print("📜 Transaction History:")
    if users[user]['transactions']:
        for i, t in enumerate(users[user]['transactions'], 1):
            print(f"{i}. {t}")
    else:
        print("No transactions found.")

def atm_interface():
    user = login()
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_balance(user)
        elif choice == '2':
            deposit(user)
        elif choice == '3':
            withdraw(user)
        elif choice == '4':
            transaction_history(user)
        elif choice == '5':
            print("👋 Thank you for using  ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

# Run the ATM
atm_interface()