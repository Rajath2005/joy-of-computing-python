# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 15:32:34 2025

@author: Rajath

"""
# Here we are using logic to print the fizzbuzz game 
for i in range(1,51):
    if(i%3==0 and i%5==0): # We have to write this befor to accept all test cases
        print(str(i)+" = FizzBUzz")
    
    elif(i%5==0):
        print(str(i)+" = Buzz")
    elif(i%3==0):
        print(str(i)+" = Fizz")
    else:
        print(str(i))