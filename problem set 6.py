from accountio import write_account
from accountio import read_account
import random

current_account = 0

def login(input_username,input_password):

    if lines[0].rstrip('\n') == input_username and lines[1] == input_password:
        return True

    else:
        return False

account_balance = 0


def get_balance():
    return float(account_balance)

def deposit(amt):
    global account_balance
    if amt <= 0:
        raise ValueError('Deposited amount is invalid')

    else:
        account_balance += amt
        return float(account_balance)

def withdraw(amt):
    global account_balance
    if amt <= 0:
        raise ValueError('Withdrawal amount is invalid')

    else:
        account_balance -= amt
        return account_balance
HISTORY = []

def message():
    print('To get balance type "b" or "B"')
    print('To deposit type "d" or "D"')
    print('To withdraw type "w" or "W"')
    print('To terminate program type "q" or "Q"')
    print('To print command history type "h" or "H"')
    print('To create new account type "n" or "N"')
    print('To select account type "a" or "A"')

def print_history():
    for char in HISTORY:
        if char[0] == 'd':
            char[0] = 'Deposit'

        else:
            char[0] = 'Withdrawal'

    for char in HISTORY:
        print(f'{char[0]} amount: {char[1]} Account balance after the {char[0]}: {char[2]}')

def do_commands():
    choice = input('Type "new" to open a new account or type "current" to manage existing account ')
    if choice == 'current':
        print('To manage current account, type "a" or "A" as your command')

    elif choice == 'new':
        print('To select account, type "n" or "N" as your command')

    global current_account
    global account_balance
    legal = ['b','d','w','q','h','n','a']
    command = input('Please input your command: ')
    command = command.lower()

    while True:
        if command in legal:
            if current_account == 0 and command in ['d','b','w','h']:
                print('Please choose an account first or create a new account')
                command = input('Please input your command: ')
                command = command.lower()

            else:
                if command == 'q':
                    current_account = 0
                    exit()

                elif command == 'b':
                    action = get_balance()
                    print(action)
                    command = input('Please input your command: ')
                    command = command.lower()

                elif command == 'd':
                    amt = float(input('Please input deposit amount: '))
                    try:
                        action = deposit(amt)
                        x = [command,amt,get_balance()]
                        HISTORY.append(x)
                        write_account(current_account, get_balance, ['deposit',amt])
                        print(account_balance)
                        command = input('Please input your command: ')
                        command = command.lower()
                    except ValueError as ve:
                        print(ve)
                        command = input('Please input your command: ')
                        command = command.lower()

                elif command == 'h':
                    print_history()
                    command = input('Please input your command: ')
                    command = command.lower()

                elif command == 'n':
                    acctnum = new_account()
                    print(f'Your new account number is {acctnum}')
                    write_account(acctnum,0,[])
                    command = input('Please input your command: ')
                    command = command.lower()

                elif command == 'a':
                    try:
                        acct = int(input('Please type the account number: '))
                        current_account = acct
                        account_balance = read_account(current_account)[0]
                        read_account(current_account)
                        message()
                        command = input('Please input your command: ')
                        command = command.lower()
                    except FileNotFoundError as ve:
                        print(ve)
                        acct = int(input('Please type the account number: '))
                        read_account(acct)

                else:
                    amt = float(input('Please input withdraw amount: '))
                    try:
                        withdraw(amt)
                        x = [command,amt,get_balance()]
                        HISTORY.append(x)
                        print(account_balance)
                        write_account(current_account, get_balance(), ['withdraw',amt])
                        command = input('Please input your command: ')
                        command = command.lower()

                    except ValueError as ve:
                        print(ve)
                        command = input('Please input your command: ')
                        command = command.lower()

        else:
            print('Invalid command. Please try again')
            command = input('Please input your command: ')
            command = command.lower()

def new_account():
    acctnum = [str(random.randint(1,9))]
    last_4 = random.sample(range(0,9),4)
    for ind,num in enumerate(last_4):
        last_4[ind] = str(num)
    for num in last_4:
        acctnum.append(num)
    
    final = int(''.join(acctnum))
    return final



if __name__ == '__main__':
    print('Welcome to money heist e-banking')
    action = input('Type "login" to login or "Change" to change username/password: ')
    action = action.lower()
    while True:
        if action == 'login':
            f = open('banking.creds','r')
            lines = f.readlines()
            f.close()
            input_username = input('Please input your username: ')
            input_password = input('Please input your password: ')

            count = 1
            while True:
                if count > 3:
                    exit()

                elif login(input_username,input_password):
                    do_commands()
                else:
                    count += 1
                    print(f'Login failed. Please try again')
                    input_username = input('Please input your username: ')
                    input_password = input('Please input your password: ')

        elif action == 'change':
            f = open('banking.creds','w')

            new_username = input('Please type in your new username: ')
            new_password = input('Please type in your new password: ')

            f.write(new_username + '\n')
            f.write(new_password)

            f.close()

            f = open('banking.creds','r')
            lines = f.readlines()
            f.close()
            action = input('Type "login" to login or "Change" to change username/password: ')
            action = action.lower()

        else:
            print('Invalid action please try again')
            action = input('Type "login" to login or "change" to change username/password: ')
            action = action.lower()
