#Simulated annealing applied to a random instance of the knapsack problem

import pdb
from random import Random  
import numpy as np
import common_functions as cf
import problem_instance as pi


t = 100000  #setting an initial temperature
M = 500    #number of iterations at each temperature
k = 0     #counter to keep track of main loop


x_init = cf.initial_solution()  #The very first or the initial solution 
f_init = cf.evaluate(x_init)    #evaluation of x_init
x_curr = np.copy(x_init)     #Current solution. Starts out with x_init
f_curr = cf.evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
print("initial solution {}".format(f_curr[0]))


#storing information for the feasible solutions
f_value = []
f_weight = []
f_solution = []

#varaible to record the number of solutions evaluated
solutionsChecked = 0


#begin local search overall logic ----------------
done = 0
    
while done == 0:
    
    #stopping criterion
    if t<1:
        done = 1
    
    m = 0        
    while m<M:
        solutionsChecked += 1
        #print("k = {}, m = {}, s = {} \n".format(k,m,solutionsChecked))

        N = cf.neighborhood(x_curr)            #create a list of all neighbors in the neighborhood of x_curr
        s = N[cf.myPRNG.randint(0,len(N)-1)]   #A randomly selected neighbor
        
        #check for feasibility of this solution
        try:
            eval_s = cf.evaluate(s)
        except:
            continue

        #If this random neighbor is an improving move, accept it immediately
        #else accept it a probability distribution
        if eval_s[0] >= f_curr[0]:
            x_curr = np.copy(s)
            f_curr = np.copy(eval_s)

            f_solution.append(x_curr)
            f_value.append(f_curr[0])
            f_weight.append(f_curr[1])
        else:
            p = np.exp(-(f_curr[0]-eval_s[0])/t)
            test_p = cf.myPRNG.uniform(0,1)
            
            if test_p<=p:
                x_curr = np.copy(s)
                f_curr = np.copy(eval_s)

                f_solution.append(x_curr)
                f_value.append(f_curr[0])
                f_weight.append(f_curr[1])
        m += 1
        print("current solution: {} \n".format(f_curr[0]))
    
    
    #incrementing k and updating functions of k
    k += 1
    t = 0.8*t  #cauchy cooling function


print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", np.nanmax(f_value))
print ("Weight is: ", f_weight[np.nanargmax(f_value)])
print ("Total number of items selected: ", np.sum(x_curr))
print ("Best solution: ", x_curr)
