from GWbankaccountClass import BankAccount

def main():
    # Get the starting balance from the user
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object with the starting balance
    savings = BankAccount(start_bal)

    # Deposit the user's paycheck
    pay = float(input('Enter how much of you rpay you would like to deposit: '))
    savings.deposit(pay)

    # Display the updated balance after deposit
    print(f'Your account balance after deposit is ${savings.get_balance():,.2f}.')

    # Get the amount to withdraw
    cash = float(input('Enter how much would you like to withdraw: '))
    savings.withdraw(cash)

    # Display the updated balance after withdrawal
    print(f'Your account balance after withdraw is ${savings.get_balance():,.2f}.')

if __name__ == '__main__':
    main()
