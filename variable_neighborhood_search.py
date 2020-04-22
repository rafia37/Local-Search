#Variable neighborhood search 
#Using variable neighborhood descent as local search method


import pdb
import logging
from datetime import datetime
from random import Random   
import numpy as np
import common_functions as cf



#-------------
#Logger Setup
#-------------

now = datetime.now()
log_fname = "log_files/vns_"+now.strftime("%m%d_%H%M")+".log"
LOG_FORMAT = "%(lineno)d %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=log_fname,
                    level=logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()




#---------------
#VND Algorithm
#---------------

#A local search algorithm
#In this case, LS is Variable Neighborhood Descent (VND) Algorithm
def LS(init_s, k=1, k_max=4):

    curr_s = np.copy(init_s)
    curr_f = cf.evaluate(init_s)

    logger.info("--------Entered VND algorithm--------\n")

    counter = 0
    while k<=k_max:
        
        logger.info("checking {}-flip neighborhood \n".format(k))     
    
        Neighborhood = cf.neighborhood(curr_s, k)   #create a list of all neighbors in the neighborhood of x_curr
    
        logger.debug("current solution {} \n".format(curr_s))
        logger.debug("current neighborhood {} \n".format(Neighborhood))
    
        s_values = [cf.evaluate(s)[0] for s in Neighborhood]
        counter += 1

        try:
            s = Neighborhood[np.nanargmax(s_values)]  #Best neighbor in the current neighborhood
        except:
            print("No feasible solution in the neighborhood")
            break
        f_s = cf.evaluate(s)
    
        #if this neighbor is better than current solution, accept this move
        if  f_s[0] > curr_f[0]:
            curr_s = np.copy(s)        
            curr_f = np.copy(f_s)
            k = 1
        else:
            k += 1
        

        logger.info("current best solution {} \n".format(curr_f[0]))
        print("current solution {} \n".format(curr_f[0]))
    
    logger.info("--------Exiting VND algorithm-------- \n")
    return curr_s, curr_f, counter




#----------
#Basic VNS
#----------

#monitor the number of solutions evaluated
solutionsChecked = 0        

#initializing current solution
x_curr = cf.initial_solution() 
f_curr = cf.evaluate(x_curr)

logger.info("initial solution and total items: {} {} \n".format(x_curr, np.sum(x_curr)))
logger.info("initial evaluation: {} \n".format(f_curr))

myPRNG = cf.myPRNG

k_max = 4   #total number of k-flip neighborhoods

done = 0    #A flag to control iterations

counter = 0     #A counter to count iterations

while done==0:
    k = 1

    while k<=k_max:
        Neighborhood = cf.neighborhood(x_curr, k)
        N_values = [cf.evaluate(s)[0] for s in Neighborhood]  #values for each solution int he neighborhood
        feasible_N = Neighborhood[np.isfinite(N_values)]   #feasible neighborhood
        solutionsChecked += 1

        #If there are no feasible solutions in the neighborhood
        #break out of the loop
        if len(feasible_N)==0:
            break

        shaking = myPRNG.randint(0,len(feasible_N)-1)      #"shaking" to get a random solution
        s0 = feasible_N[shaking]  
        s1, f_s1, c = LS(s0)
        solutionsChecked += c
        
        if f_s1[0] > f_curr[0]:
            x_curr = np.copy(s1)
            f_curr = np.copy(f_s1)
            k=1
        else:
            k += 1
    
    counter += 1 
    print(counter)
    if counter == 50:
        done = 1

        
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_curr[0])
print ("Weight is: ", f_curr[1])
print ("Total number of items selected: ", np.sum(x_curr))
print ("Best solution: ", x_curr)
