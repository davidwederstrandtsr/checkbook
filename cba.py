# Command Line Checkbook Application ver 2.0
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

# checks that the input type is correct
def check_currency_type(currency):
    '''checks a value type
        - needs to be float or int
    '''
    return type(currency) == float or type(currency) == int

# get_current_balance retrieves the last 
def get_current_balance():
    '''get current balance
        - reads the current balance from the account file
    '''
    with open(filename, "r") as f:
        current_balance = 0.00
        current_baleace = float(current_balance)
        balance = f.readlines()
        for b in balance:
            current_balance += float(b)
    return current_balance
    
# this function prints the menu
def menu():
    '''prints out a menu for the checkbook application'''
    print('\nWhat would you like to do?')
    print()
    print('1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit)\n4) display history\n5) exit\n\n')


def menu_input():
    prompt = input('Your choice? ')
    while prompt not in ['1', '2', '3', '4', '5', 'r']:
        print(f"\nInvalid choice: {prompt}")
        menu()
        prompt = input('\nYour choice: ')
    return prompt

# write new balance to file
def update_account(amount, op='c'):
    '''updates account from either withdraw or deposit'''
    with open(filename, 'a') as f:
        if op == 'w':
            f.write(f'\n{-amount}') 
        else:
            f.write(f'\n{amount}')

# make a withdraw
# def validate_debit():
#     '''performs the withdraw function
#         - receives input from user
#         - validates value type
#         - validates value as non-negative
#     '''
#     debit = float(input("How much is the debit(withdraw)? (Enter as #####.##)   $"))
#     while check_currency_type(debit) == False:
#         print(f'You entered a value that is not a currency')
#         debit = float(input("How much is the debit (withdraw)? $"))
#     while debit <= 0:
#         print(f'You entered {debit}, Please enter a value greater than $0.00')
#         debit = float(input("How much is the debit (withdraw)? $"))
#     return debit

def validate_amount(str):
    '''performs the withdraw function
        - receives input from user
        - validates value type
        - validates value as non-negative
    '''
    amount = float(input(f"\nHow much is the {str}? (Enter as #####.##)   $"))
    while check_currency_type(amount) == False:
        print(f'You entered a value that is not a currency')
        amount = float(input(f"How much is the {str}? $"))
    while amount <= 0:
        print(f'You entered {amount}, Please enter a value greater than $0.00')
        amount = float(input(f"How much is the {str}? $"))
    return amount


def check_withdraw():
    '''returns whether or not a debit is validate or not
        - reads the current balance from the account file
        - checks debit against current_balance
        - sends valid new_balance to update_account
    '''
    current_balance = float(get_current_balance())
    if current_balance <= 0:
        print('Your account balance is $0.00')
        print('You cannot make a withdraw.')
        print('Please try again later.\n')
        
    else:
        debit = float(validate_amount('debit (withdraw)'))
    
        while current_balance - debit < 0:
            print(f'Your account has insufficient funds for the amount entered. ${debit}')
            print(f'Your account balance is ${current_balance}\n')
            debit = validate_amount('debit (withdraw)')
    
        new_balance = current_balance - debit
        update_account(new_balance)
    menu()

    
# make a deposit
def check_credit():
    '''check credit
        - reads the current balance from the account file
        - checks credit is valid
        - sends valid new_balance to update_account
    '''
    current_balance = float(get_current_balance())
    credit = validate_amount('deposit (credit)')
    
    new_balance = current_balance + credit
    update_account(new_balance)

# show all of the accounts history
def show_history():
    with open(filename, 'r') as f:
        history = f.readlines()
        for h in history:
            print(h.replace('\\','').replace('n',', '))
            
# start of main
print()
print("~~~ Welcome to your terminal checkbook!~~~")
print()
while user_choice:
    menu()
    prompt = menu_input()

    print()
    # prompt 1 will only return the current balance
    if prompt == '1':
        print('Your current balance is ${:.2f}\n'.format(get_current_balance()))

    # prompt 2 will check the type of the debit
    elif prompt == '2':
        check_withdraw()

    # prompt 3 will check the type of the deposit
    elif prompt == '3':
        check_credit()
        
    # prompt 4 while print out the account's history      
    elif prompt == '4':
        show_history()
        
    elif prompt == 'r':
        clear_records()
    # exits the program
    else:
        user_choice = False
print("\nThanks, have a great day!\n")











# fixing methods





  