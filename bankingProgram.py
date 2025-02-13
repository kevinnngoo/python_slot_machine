# Python Banking Program
# 1. Show Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit



def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    amount = float(input("How much would you like to deposit: "))
    if amount < 0:
        print("That is not a valid amount")
        return balance  
    else:
        balance += amount
        print(f"You have deposited: ${amount:.2f}")
        return balance 

def withdraw(balance):
    amount = float(input("How much would you like to withdraw?: "))
    if amount > balance:
        print(f"You can't withdraw more than your balance: ${balance:.2f}")
        return balance  
    elif amount < 0: 
        print("Amount must be greater than 0.")
        return balance  
        balance -= amount
        print(f"You have withdrawn ${amount:.2f}")
        return balance 

def main():
    balance = 0
    is_running = True 

    while is_running: 
        print("\nWelcome to the Bank!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = deposit(balance)  
        elif choice == 3:
            balance = withdraw(balance)  
        elif choice == 4:
            is_running = False
        else:
            print("Please choose a valid option.")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
