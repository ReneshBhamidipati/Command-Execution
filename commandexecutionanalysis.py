#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:58:23 2019

@author: reneshbhamidipati

This program calculates the differences between timestamps in order to find 
the execution time of a specific command. This process repeats for multiple 
commands, provided in the command_history.txt input file. This program also 
calculates the number of times that each respective command was used;
this is recorded onto the command_history_out.txt output file.

"""
from datetime import datetime 

# Open the input file and read all the timestamps and commands.
with open('/Users/reneshbhamidipati/Documents/command_history.txt') as f:
    lines = f.readlines() 
    
# Create two lists; one for collecting the timestamps 
# and one for collecting the commands.
ts_lst = []
command_lst = []
l = len(lines)

# Use a for loop to access the timestamps and commands from the input file, 
# and then add each to their respective lists.
for i in range(0,l-1,2):
    #print(lines[i])
    ts = datetime.fromtimestamp(int(lines[i][1:]))
    command = lines[i+1]
    ts_lst.append(ts)
    command_lst.append(command)      
    
# Create an output file.
wf = open('/Users/reneshbhamidipati/Documents/command_history_out.txt', 'w')

ts_len = len(ts_lst)

# Create a for loop that calculates the difference between timestamps; this 
# number (in seconds) will give you the execution time of each command 
# in the input file.
for i in range(0,ts_len-1):
    diff = (ts_lst[i+1] - ts_lst[i])
    seconds = diff.total_seconds()
    print(seconds)
    print(command_lst[i])
    wf.write(command_lst[i].rstrip('\n')+"--> "+str(seconds)+"\n")

# Create a dictionary that calculates the frequency of each command used
# in the input file.
d = dict()
for i in command_lst:
    s = i.split(" ")
    #print(s)
    key = s[0]
    if key.endswith('\n'): 
        key = key.rstrip('\n')
    # Looks up a command in the dictionary, and finds if it even exists 
    # in the dictionary. If the command already exists in the dictionary, 
    # then it will incrememnt the value of that command by 1. This number 
    # shows how many times that command is used. If the command does not exist
    # in the dictionary, then it will add that command to the dictionary.
    if key in d.keys():
        d[key] = d[key] + 1
    else: 
        d[key] = 1
print(d)

# Once you've compiled the commands with their frequencies used, you write 
# this information into the output file.
for key in d.keys(): # this is equivalent to "for i in ___"
    value = d[key]
    wf.write("Command: "+key+" ; No. of times used: "+ str(value)+"\n")

wf.close()
