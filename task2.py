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
        highestValue ={
            "time": 0,
            "telephone": ""
        }
    for i in range(len(calls)): #time O(n)
        currentValue = calls[i]
        time = int(currentValue[3])
        sender = currentValue[0]
        receiver = currentValue[1]
        setofData[sender] = int(setofData[sender]) + time if sender in setofData else time
        setofData[receiver] = int(setofData[receiver]) + time if receiver in setofData else time 
        higherrowValue = sender if setofData[sender] > setofData[receiver] else receiver
        highestValue = newHighestValue(higherrowValue,setofData[higherrowValue]) if highestValue["time"] < setofData[higherrowValue] else highestValue 
    return highestValue


# In[5]:


finalData = read_csv_data("./calls.csv")
print(finalData["telephone"] +" spent the longest time, total "+ str(finalData["time"]) +" seconds, on the phone during September 2016");


# Runtime Analysis <br/>
# - The time Complexity for the problem is O(3n+k) which is equvivalent to O(n), where k is a constant, k<=50 <br/>
# - The best case would be O(3n+k).<br/>
# - The worst case would be O(3n+k).<br/>





