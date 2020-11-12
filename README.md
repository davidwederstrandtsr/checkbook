#                    Checkbook Application
- cba.py is the updated version or version 2.0
    - added some secutiry feature
    - made methods that do only one thing instead of several things

##      This application simulates a bank account

## Method:
#### check_currency_type
- checks debits and deposits
- takes user's input amount
    - return ture if amount is a float or int
    
### get_current_balance
- opens the account file
- calcuates and returns the current balence

### menu
- prints the menu anytime it is called

### menu_input
- request a valid input from the user
- 'r' is include for a work in progress

### upate_account
- open the account file with write priviledge
- writes amount to modify account by
    - debit = '-amount'
    - deposit = 'amount'
    
### validate_amount(str)
- str equals 'debit' or 'deposit'
- checks the type of either withdraw or deposit
- checks if amount if greater then 0.00

### check_withdraw
- checks if account is greater than 0
- updates the account if valid

### check_credit
- checks if value is valid and updates file

### show_history
- opens account file
- shows transactions in order

### main
- this is the main part of the 
