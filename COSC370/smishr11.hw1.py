#!/usr/bin/env python3

# Homework 1: Using Matplotlib to Graph Temperature Data
# COSC370
# Swasti Mishra // netid: smishr11
# July 15, 2022

# Data/Code from assignment
from numpy import arange
import matplotlib.pyplot as plt
xData = arange(1,32)
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = [86.]

# 'i' increments through the temperature data, and 'tempTotal' is a running 
# total of all the temperature data. 
i = 0               
tempTotal = 0 

# Calculates the monthly running average
for x in tData :
	tempTotal += x
	i += 1
	avg.append(tempTotal/i)

# Prints the averages in a table (I did mine in markdown format)
print('| Average | Day |')
print('|---------|-----|')
i = 1
for x in avg :
    print('|', ('{:.2f}'.format(x)).center(8), end='|')
    print(str(i).center(5), end='|')
    print('')
    i += 1

# Creates graph 
#   Red Points: Original Data
#   Blue Line: Connects Original Data
#   Green Dashed Line: Shows Change in Average High 
# Other Details:
#   'bo-' is styling for the original data points and connecting line
#   'g--' makes the average line green and dashed
plt.title('High Temperatures for Knoxville, TN - August 2013')
plt.xlabel('Day')
plt.ylabel('High Temp')
plt.grid(ls = ':')
plt.xlim(0, 32)
plt.ylim(70, 95)
plt.plot(xData, tData, 'bo-', markerfacecolor = 'red')
plt.plot(avg, 'g--')
plt.text(14, 86, "Monthly Avg", color = 'green')

# Display graph
plt.show()