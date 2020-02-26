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
        init_balance = 0.00
        f.write(init_balance)
        print('Account created, initial balance is ${:.2f}\n'.format(init_balance))      

# get_current_balance retrieves the last 
def get_current_balance():
    with open(filename, "r") as f:
        current_balance = 0.00
        balance = f.readlines()
        for b in balance:
            current_balance += float(b)
    return current_balance

# make a withdraw
def withdraw(debit):
    message = ''
    debit = float(debit)
    current_balance = get_current_balance()
    current_balance = float(current_balance)
    if debit <= current_balance:
        with open(filename, 'a') as f:
            f.write(f'\n{-debit}')
    else:
        return print("Insuffient Funds")
    
 
# make a deposit
def credit(deposit):
    message = ''
    deposit = float(deposit)
    current_balance = get_current_balance()
    if deposit >= 1:
        with open(filename, "a") as f:
            f.write(f'\n{deposit}')
    else:
        return print("You entered a value ")
    
# show all of the accounts history
def show_history():
    with open(filename, 'r') as f:
        history = f.readlines()
        for h in history:
            print(h.replace('\\','').replace('n',', '))

# this function prints the menu
def menu():
    print('What would you like to do?')
    print()
    print('1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit)\n4) display history\n5) exit\n\n')

# start of main

print()
print("~~~ Welcome to your terminal checkbook!~~~")
print()
while user_choice == True:
    menu()
    prompt = input('Your choice? ')
    while prompt not in ['1', '2', '3', '4', '5']:
        print(f"\nInvalid choice: {prompt}")
        menu()
        prompt = input('\nYour choice? ')
        
    print()
    if prompt == '1':
        print('Your current balance is ${:.2f}\n'.format(get_current_balance()))
    elif prompt == '2':
        debit = input("How much is the debit? $")
        withdraw(debit)
    elif prompt == '3':
        deposit = input("How much is the deposit? $")
        credit(deposit)
    elif prompt == '4':
        show_history()
    else:
        user_choice = False
print("\nThanks, have a great day!\n")