#!/usr/bin/env python
# coding: utf-8

# <h4>Task 0 </h4>
# <br/>
#     <p><b>Print this message</b></p> 
#  <ol>
#     <li>First record of texts, <b>incoming number</b> texts <b>answering number </b> at time <b>time</b></li>
#     <li>Last record of calls, <b>incoming number</b> calls <b>answering number</b> at time <b>time.</b></li>
# </ol>

# In[2]:


import csv


# In[3]:


def read_csvFiles(filename, arguments):
    with open(filename,'r') as f:
        reader = csv.reader(f) # time  O(n)
        data = list(reader)  # time  O(n)
    index = 0 if arguments == "first" else len(data)-1  # time  O(1) or O(2) 
    return data[index]    #time O(1)


# In[4]:


textsData = read_csvFiles("texts.csv", "first") # time O(2n)
callData= read_csvFiles("calls.csv", "last")[0] # time O(2n)
print("First record of texts, "+ textsData[0] + " texts " + textsData[1] + " at time " + textsData[2] + ".")# time O(4)
print("First record of calls, "+ callData[0] + " calls " + callData[1] + " at time " + callData[2] + ", lasting " + callData[3] + " seconds")# time O(4)


# Runtime Analysis for this Task <br/>
# - The time Complexity for the problem is O(4n+8) which is equvivalent to O(n) <br/>
# - The best case would be O(4n+8) when finding the first element from the list.<br/>
# - The worst case would be O(4n+8) when finding the last element from the list.<br/>
# 






