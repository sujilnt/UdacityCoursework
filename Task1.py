"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# analysing cols data
'''
import qgrid
import pandas as pd
df = pd.read_csv("./calls.csv", names=["sender","receiver","call_time","duration"])
qgrid.show_grid(df)
'''


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
