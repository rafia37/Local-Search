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
        raise ValueError

    return [totalValue, totalWeight]   #returns a list of both total value and total weight
          
       

#1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(np.copy(x))
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
    
    return x


t = 15000  #setting an initial temperature
M = 10    #number of iterations at each temperature
k = 0     #counter to eep track of main loop


x_curr = initial_solution()  #x_curr will hold the current solution 
#x_curr = np.zeros(n,dtype=int)
f_curr = evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
print("initial solution {}".format(f_curr[0]))

#varaible to record the number of solutions evaluated
solutionsChecked = 0



#begin local search overall logic ----------------
done = 0
    
while done == 0:
    m = 0        
    while m<M:
        solutionsChecked += 1
        print("k = {}, m = {}, s = {} \n".format(k,m,solutionsChecked))

        N = neighborhood(x_curr)            #create a list of all neighbors in the neighborhood of x_curr
        s = N[myPRNG.randint(0,len(N)-1)]   #A randomly selected neighbor
        
        #check for feasibility of this solution
        try:
            eval_s = evaluate(s)
        except:
            continue

        #If this random neighbor is an improving move, accept it immediately
        #else accept it a probability distribution
        if eval_s[0] >= f_curr[0]:
            x_curr = np.copy(s)
            f_curr = np.copy(eval_s)
        else:
            p = np.exp(-(f_curr[0]-eval_s[0])/t)
            test_p = myPRNG.uniform(0,1)
            
            if test_p<=p:
                x_curr = np.copy(s)
                f_curr = np.copy(eval_s)
        m += 1
    
    #stopping criterion
    if k==10:
        done = 1
    #incrementing k and updating functions of k
    k += 1
    t = t/(1+k)  #cauchy cooling function

print("final solution {}".format(f_curr[0]))
print("solutions checked: {}".format(solutionsChecked))

"""
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
"""