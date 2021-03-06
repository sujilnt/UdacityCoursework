#!/usr/bin/env python
# coding: utf-8

# #### Task - 2
# <br/>
# <b> Which telephone number spent the longest time on the phone during the period?  Don't forget that time spent answering a call is also time spent on the phone.</b><br/>
# <ol>
#     <b>Print this message</b>
#   <li><b>telephone number</b> spent the longest time, <b>total time</b> seconds, on the phone during September 2016.</li>
# </ol>

# In[3]:


import csv

def newHighestValue(key,value):
    return {
        "time":value,
        "telephone": key
    }
    
    
def read_csv_data(filename):
    setofData={};
    with open(filename,'r') as f:
        reader = csv.reader(f)  #time O(n)
        calls = list(reader) #time O(n)
        highestValue ={}
    for i in range(len(calls)): #time O(n)
        currentValue = calls[i]
        time = int(currentValue[3])
        sender = currentValue[0]
        receiver = currentValue[1]
        setofData[sender] = int(setofData[sender]) + time if sender in setofData else time
        setofData[receiver] = int(setofData[receiver]) + time if receiver in setofData else time
        highestValue = max(zip(setofData.values(), setofData.keys()))
    return highestValue


# In[5]:

finalData = read_csv_data("./calls.csv")
print(finalData[1] + " spent the longest time, total " + str(finalData[0]) + " seconds, on the phone during September 2016");





