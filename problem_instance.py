#A Random problem instance for knapsack problem

import numpy as np
from random import Random

seed = 5113
myPRNG = Random(seed)

#Number of available items or,
#number of elements in a solution
n = 150    


#values and weights of items for the knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))
    

#Maximum weight limit for the knapsack
maxWeight = 1500        

