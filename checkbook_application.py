#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[19]:


filename = "checkbook_application_data.txt"
with open(filename, "w") as f:
    f.write('100.00')


# In[22]:


def get_balance():
    balance = ''
    with open(filename, "r") as f:
        balance = f.readlines()
    return float(balance[0])


# In[23]:


print(get_balance())


# In[ ]:




