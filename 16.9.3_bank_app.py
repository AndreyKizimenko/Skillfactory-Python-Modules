class Client():

    def __init__(self,name,first_deposit=0):
        self.name = name
        self.balance = first_deposit

    def __str__(self):
        return f'{self.name}, your current balance is {self.balance}'

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f'Not enough funds on the account. Your current balance is {self.balance}')
            raise EnvironmentError('THis is an error')


# Making a deposit
def make_deposit():
    while True:
        try:
            new_client.deposit(int(input('How much you want to deposit ')))
        except:
            print('Please enter an amount')
        else:
            print(f'Deposit accepted. New balance is {new_client.balance}')
            break


# Withdraw money
def make_withdrawal():
    while True:
        try:
            new_client.withdraw(int(input('How much you want to withdraw ')))
        except:
            print('Please enter an amount')
        else:
            print(f'Withdrawal accepted. New balance is {new_client.balance}')
            break


#Check current balance
def check_balance():
    print(new_client)


# APP RUNNING

# Opening a new account
while True:
    try:
        new_client = Client(input('What is your name? '), int(input('What is the initial deposit? ')))
    except:
        print('Please enter an amount')
    else:
        print(f'Account opened. Your balance is {new_client.balance}')
        account_open = True
        break

while account_open:

    choice = 'Place Holder'
    if new_client.balance <= 0:
        while choice not in ['b', 'd']:
            choice = input('What do you want to do? Type: B for balance, D for deposit').lower()
    else:
        while choice not in ['b', 'd', 'w']:
            choice = input('What do you want to do? Type: B for balance, D for deposit or W for withdrawal ').lower()

    if choice == 'b':
        check_balance()
    elif choice == 'd':
        make_deposit()
    else:
        make_withdrawal()

    anything_else = 'Place Holder'
    while anything_else not in ['y','n']:
        anything_else = input('Do you want to do anything else? (Y or N)').lower()

    if anything_else == 'y':
        continue
    else:
        print('Thank you for using our bank. Have a wonderful day!')
        break


