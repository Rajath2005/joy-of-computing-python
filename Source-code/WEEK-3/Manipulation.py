# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:22:43 2025

@author: araja
"""
#Manipulation 

#We created a list  beelow.
shopping=["Coffee","Sugar","Milk","Curd"]

#Using for loops to print the items present in the list.
for item in shopping:
    print(item) # printing the items present.
    
print("\n")    

# we can insert items at certain position using methods

shopping.append("Biscuit")#TThis can't at at ceratin Position for that we have to incert the insert function

shopping.insert(2,"Coffe Powder")


#Printing Using indexes
for i in range(6):
    print(shopping[i])

ages=[12,23,45,67,8,1,33,44,55,66,77,23,43,5,6,7,89,22,4,5,6,12,12,12,12,2,3,4]

#Using another function called count to count the numbers

print(f"\nThe entered age is presnt",ages.count(12),"times in the list")

#We are used len to find the length of the list

print("Number of persons ages in the list is:",len(ages),"\n")

#We can use len function to iterate through the loops
print("Here we are Printing the Shopping List Using len function in for loop")
for i in range(len(shopping)):
    print(shopping[i])