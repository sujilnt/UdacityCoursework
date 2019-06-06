#!/usr/bin/env python
# coding: utf-8

# ####  TASK 4:
# <bold>The telephone company want to identify numbers that might be doing
# telephone marketing. Create a set of possible telemarketers: <br/>
#  - These are numbers that make outgoing calls but never send texts,receive texts or receive incoming calls.</bold>

# In[12]:


import csv


def read_csv_files(filename):
    with open(filename,"r") as f:
        marketer_list={};
        reader = csv.reader(f); # time O(n)
        caller = list(reader) # time O(n)
        caller_data_length = range(len(caller)) # time  O(2)
        for i in caller_data_length: # time O(n)
            out_caller = caller[i][0]
            receiver = caller[i][1]
            if (out_caller[:3] == "140") | (receiver[:3]=="140"):
                if out_caller[:3] == "140":
                    marketer_list[out_caller] = out_caller
                else:
                    del marketer_list[receiver]  # if receives call then delete the number
        return marketer_list
# In[14]:


def compare(marketerlist, textList):
    finalist = marketerlist;
    for key in finaList:
        if key in textList:
            del finalist[key]
    return sorted(finalist)


marketerlist = read_csv_files("./calls.csv")
textList = read_csv_files("./texts.csv") # check for 140 , if found push to dictionary
finaList = marketerlist if(len(textList) == 0 ) else compare(marketerlist, textList)
print("These numbers could be telemarketers:")
for marketer in finaList: # O(n)
    print(marketer)
    





