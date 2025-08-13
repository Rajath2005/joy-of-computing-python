# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 18:33:05 2025

@author: araja
"""
# A list defined as ages
ages=[1,2,3,4,5,6,7,1,23,34,56,78,98,76,54,34,22,11,33,44,55,66,77,88,33,3,3,3]


# Here we are using operation to sort the list
ages.sort()

print("Ages after Sorting:")
for i in range(len(ages)):
    print(i,end=" ")
    
# here we are printing in reverse order(Descending)

ages.reverse()

print("\n\nAges after Reverse Sorting:")
for i in range(len(ages)):
    print(ages[i],end=" ")
    
print("\n\nNames Printing:")

# Here we are creating one list contain the names of the students

students=["Rajath","Kiran","Sheethal","Rithesh","Sanath"]
students.sort()

for i in students:
    print(i)