# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:32:51 2025

@author: araja
"""
from statistics import mean # Here we are importing the mean

from scipy import stats
# Here we are taken the some data set 
Estimate=[690, 682, 437, 615, 451, 527, 406, 338, 585, 521,
580, 526, 358, 451, 642, 393, 634, 417, 587, 391,
352, 600, 494, 572, 495, 593, 358, 602, 493, 339,
486, 580, 311, 365, 514, 328, 313, 319, 345, 391,
318, 534, 603, 530, 532, 453, 526, 567, 368, 400,
411, 497, 546, 512, 312, 421, 619, 532, 385, 390,
410, 383, 673, 515, 491, 329, 413, 564, 543, 501,
607, 483, 627, 688, 603
]

# We are sorting it using sort function

Estimate.sort()
m=stats.trim_mean(Estimate,0.1) # In python we can directly by using built in function
print(m)

#for i in range(len(Estimate)):
#    print(Estimate[i])   

#tv=int(0.1*len(Estimate)) # This is to find the 10% of the list
#Estimate=Estimate[tv:] # This is to remove the 10% smallest
#Estimate=Estimate[:len(Estimate)-tv] # This is to remove the 10% of the largest

#print(mean(Estimate))