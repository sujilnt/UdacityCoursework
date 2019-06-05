#!/usr/bin/env python
# coding: utf-8

# ####  TASK 4:
# <bold>The telephone company want to identify numbers that might be doing
# telephone marketing. Create a set of possible telemarketers: <br/>
#  - These are numbers that make outgoing calls but never send texts,
# receive texts or receive incoming calls.</bold>

# In[12]:


import csv

def read_csv_files(filename):
    with open(filename,"r") as f:
        marketer_list={};
        reader = csv.reader(f); # time O(n)
        caller = list(reader) # time O(n)
        caller_data_length= range(len(caller)) # time  O(2)
        for i in caller_data_length: # time O(n)
            out_caller = caller[i][0]
            if out_caller[:3] == "140" : 
                marketer_list[out_caller] = out_caller
        return marketer_list


# In[14]:


marketerlist = read_csv_files("./calls.csv")
print("These numbers could be telemarketers:")
for marketer in marketerlist: # O(n)
    print(marketer)
    





