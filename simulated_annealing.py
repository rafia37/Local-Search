#Simulated annealing
#author: Charles Nicholson

#Student name: Rafia Bushra
#Date: 4/13/2020

import pdb
from random import Random  
import numpy as np


#using a particular seed to generate random numbers
seed = 5113
myPRNG = Random(seed)

#number of elements in a solution
n = 150

#create an "instance" for the knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))
    
#define max weight for the knapsack
maxWeight = 1500



#monitor the number of solutions evaluated
solutionsChecked = 0

#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    
    if totalWeight > maxWeight:
        print ("Oh no! The solution is infeasible!  What to do?  What to do?")   #you will probably want to change this...

    return [totalValue, totalWeight]   #returns a list of both total value and total weight
          
       

#1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
      
    return nbrhood
          


#create the initial solution
def initial_solution():
    
    # ratio of valyes to weights 
    r = np.array(value)/np.array(weights) 
    sorted_ind = np.argsort(r)[::-1]    #sorting r in descending order
    sorted_w = np.array(weights)[sorted_ind]      #sorting weights array according to sorted ratio      
    
    #indices of 1s in solution array
    ones_ind = [j for (i,j) in enumerate(sorted_ind) if sum(sorted_w[:i+1])<maxWeight]
    
    #creating initial solution
    x = np.zeros(n, dtype=int)
    x[ones_ind] = 1
    pdb.set_trace()
    return x

initial_solution()




#varaible to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution()  #x_curr will hold the current solution 
x_best = x_curr[:]           #x_best will hold the best solution 
f_curr = evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
f_best = f_curr[:]



#begin local search overall logic ----------------
done = 0
    
while done == 0:
            
    Neighborhood = neighborhood(x_curr)   #create a list of all neighbors in the neighborhood of x_curr
    
    for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        if evaluate(s)[0] > f_best[0]:   
            x_best = s[:]                 #find the best member and keep track of that solution
            f_best = evaluate(s)[:]       #and store its evaluation  
    
    if f_best == f_curr:               #if there were no improving solutions in the neighborhood
        done = 1
    else:
        
        x_curr = x_best[:]         #else: move to the neighbor solution and continue
        f_curr = f_best[:]         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_best)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
