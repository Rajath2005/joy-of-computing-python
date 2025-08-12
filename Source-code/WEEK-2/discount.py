# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 18:30:06 2025

@author: araja
"""

# Input the cost of the item
cost = input("What is the cost? ")

# Convert the input (which is a string) to an integer
d = int(cost)

# Calculate the discounted price (10% discount)
discounted_price = 0.9 * d

# Print the discounted price
print("The cost after a 10% discount is:", discounted_price)