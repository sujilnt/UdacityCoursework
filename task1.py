#!/usr/bin/env python
# coding: utf-8

# ####  Task - 1
# <bold>Print a message </bold> <br/>
# <ol>
#     <li><bold>How many different telephone numbers are there in the records?</bold></li>
#     <li><bold>There are <count> different telephone numbers in the records.</bold></li>
# </ol>

# In[4]:


import csv
telephone_number = set()

# In[36]:

# total_different_Total_Number = > returns set of unique of numbers out of the record 
def total_different_Total_Number(filename,telephone_number_set): 
    with open(filename, 'r') as f:
        remove_duplicates_data=telephone_number_set;  # putting all the phone numbers in set to remove duplicates time # 1
        reader = csv.reader(f) # time O(n) 
        for val in reader: # time O(n)
            remove_duplicates_data.add(val[0]) # time O(1) 
            remove_duplicates_data.add(val[1]) # time O(1)  
    return telephone_number


# In[38]:


# finding the unique numbers and saving to variable telephone_number of type set . 
telephone_number = total_different_Total_Number("./calls.csv", telephone_number) # for calls.csv   # time O(2n+2)')
different_numbers = total_different_Total_Number("./texts.csv", telephone_number) # for texts.csv # time O(2n+2)')


# In[40]:

print("There are "+ str(len(different_numbers)) +" different telephone numbers in the records") # time O(3)


# Runtime Analysis <br/>
# - The time Complexity for the problem is O(4n+7) which is equvivalent to O(n) <br/>
# - The best case would be O(4n+7).<br/>
# - The worst case would be O(4n+7).<br/>
# 



