#Variable neighborhood search with variable neighborhood descent as search method
#author: Charles Nicholson

#Student name: Rafia Bushra
#Date: 04/15/20

import pdb
from random import Random   
import numpy as np


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
        totalValue = np.nan

    return [totalValue, totalWeight]   #returns a list of both total value and total weight
          
       

#1-flip neighborhood of solution x         
def neighborhood(x, k=1):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(np.copy(x))
        for j in range(k):
            #setting up circular addition
            if (i+j)>0:
                a = i+j-150
            else:
                a = i+j

            if nbrhood[i][a] == 1:
                nbrhood[i][a] = 0
            else:
                nbrhood[i][a] = 1
            
    return nbrhood
          


#create the initial solution
def initial_solution():
    sorted_w = np.sort(weights)
    
    temp_w = 0  #weight tracker
    i = len(weights) - 1 #counter that's going to count down
    num_ones = 0 #number of 1s I need in my solution
    
    #A while loop to ensure that the initial solution is not going to be infeasible
    while temp_w <= maxWeight:
        temp_w += sorted_w[i]
        i -= 1
        num_ones += 1
    
    x = np.zeros(n, dtype=int) #initializing solution array
    best_val_ind = np.argsort(value)[-num_ones:] #indices of the first few (=num_ones) highest values
    x[best_val_ind] = 1 #taking some highest value items
        
    return x




#varaible to record the number of solutions evaluated
solutionsChecked = 0

#initializing current solution
x_curr = initial_solution() 
f_curr = evaluate(x_curr)



#begin local search overall logic ----------------
k_max = 5   #total number of k-flip neighborhoods
k = 1       #starting with 1-flip neighborhood 
    
while k<=k_max:
    print("checking {}-flip neighborhood".format(k))     
    
    Neighborhood = neighborhood(x_curr, k)   #create a list of all neighbors in the neighborhood of x_curr
    solutionsChecked += len(Neighborhood)

    s_values = [evaluate(s)[0] for s in Neighborhood]
    s = Neighborhood[np.nanargmax(s_values)]  #Best neighbor in the current neighborhood
    f_s = evaluate(s)
    
    #if this neighbor is better than current solution, accept this move
    if  f_s[0] < f_curr[0]:        
        x_curr = np.copy(s)        
        f_curr = np.copy(f_s)
        k = 1
    else:
        k += 1

    print("current best solution {}".format(f_curr[0]))
        
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_curr[0])
print ("Weight is: ", f_curr[1])
print ("Total number of items selected: ", np.sum(x_curr))
print ("Best solution: ", x_curr)
