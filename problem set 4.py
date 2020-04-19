#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 05:53:44 2020

@author: dawnstaana
"""

def login(input_username,input_password):
    username = 'python'
    password = '2157'
    
    if username == input_username and password == input_password:
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

def print_history():
    for char in HISTORY:
        if char[0] == 'd':
            char[0] = 'Deposit'

        else:
            char[0] = 'Withdrawal'

    for char in HISTORY:
        print(f'{char[0]} amount: {char[1]} Account balance after the {char[0]}: {char[2]}')

def do_commands():
    message()
    legal = ['b','d','w','q','h']
    command = input('Please input your command: ')
    command = command.lower()
    
    while True:
        if command in legal:
            if command == 'q':
                exit()
        
            elif command == 'b':
                action = get_balance()
                print(action)
                command = input('Please input your command: ')
                command = command.lower()

            elif command == 'd':
                amt = input('Please input deposit amount: ')
                try:
                    action = deposit(int(amt))
                    x = [command,amt,get_balance()]
                    HISTORY.append(x)
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

            else:
                amt = int(input('Please input withdraw amount: '))
                try:
                    action = withdraw(amt)
                    x = [command,amt,get_balance()]
                    HISTORY.append(x)
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

if __name__ == '__main__':
    print('Welcome to money heist e-banking')
    input_username = input('Please input your username: ')
    input_password = input('Please input your password: ')

    count = 0

    while True:
        if count == 3:
            exit()

        elif login(input_username,input_password):
            action = do_commands()

        else:
            count += 1
            print(f'Login failed. You have {3-count} attempts left')
            input_username = input('Please input your username: ')
            input_password = input('Please input your password: ')
