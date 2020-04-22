#Common functions needed in most local search procedures

import numpy as np
import problem_instance as pi


#importing problem-specific variables
myPRNG = pi.myPRNG
value = np.array(pi.value)
weights = np.array(pi.weights)
maxWeight = pi.maxWeight
n = pi.n

#function to evaluate a solution x
def evaluate(x):
    
    totalValue = np.dot(x,value)     #compute the value of the knapsack selection
    totalWeight = np.dot(x,weights)    #compute the weight value of the knapsack selection
    
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
            
    return np.array(nbrhood)
          


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

