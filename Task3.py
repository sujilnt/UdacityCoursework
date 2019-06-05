#!/usr/bin/env python
# coding: utf-8

# ### Task3
# <p>
# (080) is the area code for fixed line telephones in Bangalore.Fixed line numbers include parentheses, so Bangalore numbers
# have the form (080)xxxxxxx.
# </p>

# In[3]:


import csv


# In[6]:


def read_csv_calls(filename,prefix):
    count=0
    totalcalls=0;
    areacodes={};
    with open(filename, 'r') as f:
        reader = csv.reader(f) # time O(n)
        calls = list(reader)   # time O(n)
        for i in range(len(calls)):
            caller = calls[i][0]  # time O(2)
            receiver= calls[i][1]; # time O(2)
            count = count +1 if ((caller[:len(prefix)] == prefix[:len(prefix)]) & (receiver[:len(prefix)] == prefix[:len(prefix)])) else count 
            totalcalls = totalcalls + 1 if ((caller[:len(prefix)] == prefix[:len(prefix)])) else totalcalls
            if(caller[:len(prefix)] == prefix[:len(prefix)]):
                areacodes[caller] = caller 
    percentage = count / totalcalls 
    return {
       "percentage": round(percentage,2)*100,
       "codes": areacodes # length 99 
   }


# In[8]:

data = read_csv_calls("./calls.csv","(080)")
print("The numbers called by people in Bangalore have codes:")
for code in data["codes"]: # time O(n)
    print(code)


# In[59]:

print(str(data["percentage"]) +" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


# Runtime Analysis for this Task <br/>
# - The time Complexity for the problem is O(3n+k) which is equvivalent to O(n), where k is a constant , where k<=50 <br/>
# - The best case would be O(3n+k).<br/>
# - The worst case would be O(3n+k).<br/>





