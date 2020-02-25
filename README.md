# Checkbook Application

## This application sinulates a bank account

### View Current Balance
    - displays the current balance

### Record a debit (withdraw)
    - checks current balance for available funds and debits if possible


### Record a credit (deposit)
    - adds funds to current balance

### Exit
    - closes the application


Application example

    $ python checkbook.py

    ~~~ Welcome to your terminal checkbook! ~~~

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 5
    Invalid choice: 5

    Your choice? 1

    Your current balance is $100.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 2

    How much is the debit? $50

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 1

    Your current balance is $50.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 4

    Thanks, have a great day!
