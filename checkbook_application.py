# Command Line Checkbook Application
# You will be creating a command line checkbook application that allows users to track their finances with a command line interface.

# When run, the application should welcome the user, and prompt them for an action to take:

# view current balance
# add a debit (withdrawal)
# add a credit (deposit)
# exit
# The application should persist between times that it is run, that is, if you run the application, 
# add some credits, exit the application and run it again, you should still see the balance that you 
#previously created. In order to do this, your application will need to store it's data in a text file. 
# Consider creating a file where each line in the file represents a single transaction.
import os.path
from os import path

filename = "checkbook_application_data.txt"
user_choice = True

if not path.exists(filename):
    with open(filename, "w") as f:
        f.write('0.00')
    print("Account created, inital balance: $0.00") 

# get_current_balance retrieves the last 
def get_current_balance():
    with open(filename, "r") as f:
        current_balance = 0
        balance = f.readlines()
        for b in balance:
            current_balance += float(b)
    return f"Your current balance is: $ {round(float(current_balance), 2)}"

# make a withdraw
def withdraw(debit):
    message = ''
    debit = float(debit)
    current_balance = float(get_current_balance())
    if debit < current_balance:
        with open(filename, 'a') as f:
            f.write(f'\n{-debit}')
        message = get_current_balance()
    else:
        message = -1 
    return message
 
# make a deposit
def credit(deposit):
    message = ''
    deposit = float(deposit)
    current_balance = float(get_current_balance())
    if deposit > 0:
        with open(filename, "a") as f:
            f.write(f'\n{deposit}')
        message = get_current_balance()
    else: # current not working
        message = -1
    return message


def menu():
    print('What would you like to do?')
    print()
    print('1) view current balance\n\
    2) record a debit (withdraw)\n\
    3) record a credit (deposit)\n\
    4) exit')
    print(f'You entered {type(prompt)}')
    return prompt

# start of main

    

print()
print("~~~ Welcome to your terminal checkbook!~~~")
print()
while user_choice == True:
    menu()
    prompt = input(': ')
    while prompt not in ['1', '2', '3', '4']:
        print("Not a valid entry!")
        menu()
        prompt = input(': ')
    
    if prompt == '1':
        get_current_balance()
    elif prompt == '2':
        debit = input("How much is the debit? $")
        resp = withdraw(debit)
        while resp == -1:
            print('You do not have enough in account to cover this withdraw.')
            debit = input("How much is the debit? $")
            resp = withdraw(debit)
        print(resp)
    elif prompt == '3':
        deposit = input("How much is the deposit? $")
        resp = credit(deposit)
        while resp == -1:
            print('You enter a dollar amount of less then or equal to 0')
            deposit = input("How much is the deposit? $")
            resp = credit(deposit)
        print(resp)
    else:
        user_choice = False
print("Thanks, have a great day")
        
            
        
        