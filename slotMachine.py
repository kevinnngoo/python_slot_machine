# Python Slot Machine Game

import random 

# Function to display current balance
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

# Function to generate a random slot row
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

# Function to print the slot row with formatting
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

# Function to determine payout based on matching symbols
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # If all symbols match
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0  # No payout if symbols don't match

# Main function to run the slot machine game
def main():
    balance = 100  # Starting balance
    print("Welcome to Python Slots!")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("********************")
    
    while balance > 0:  # Keep running until the balance is 0
        show_balance(balance)  # Show balance before betting

        # Get valid bet amount from the user
        bet_amount = input("Place your bet amount: ")
        
        if not bet_amount.isdigit():  
            print('Please input a valid number.')
            continue

        bet = int(bet_amount)

        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet <= 0:
            print("Please bet a positive amount.")
            continue

        # Deduct bet from balance
        balance -= bet

        # Spin the slots
        row = spin_row()
        print("\nSpinning.....\n")
        print_row(row)

        # Check payout
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, you lost this round.")

        # Update balance with winnings
        balance += payout
        show_balance(balance)  # Show updated balance

        # Ask if the player wants to continue
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        
        if play_again != 'Y':
            break

    # End game message
    print("********************")   
    print(f'Game over! Your final balance is ${balance:.2f}')
    print("********************")

if __name__ == '__main__':
    main()
