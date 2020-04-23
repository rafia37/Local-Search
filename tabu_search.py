import pdb
import logging
from datetime import datetime
from random import Random   
import numpy as np

#importing local modules
import common_functions as cf
import ts_functions as ts



#-------------
#Logger Setup
#-------------

now = datetime.now()
log_fname = "log_files/ts_"+now.strftime("%m%d_%H%M")+".log"
LOG_FORMAT = "%(lineno)d %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=log_fname,
                    level=logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()



#--------------
#Initializing
#--------------

#Monitoring number of solutions checked
solutionsChecked = 0

#initial solution and evaluation
x_curr = cf.initial_solution()
f_curr = cf.evaluate(x_curr)

#memory initialization
sMem, sMemVal = ts.st_memory(init=True)

#initial neighborhood
N = cf.neighborhood(x_curr)

pdb.set_trace()

#----------------------
#Tabu Search Algorithm
#----------------------

#A flag to control number of iterations
done = 0

#A counter to count number of iterations
counter = 0

#keeping track of all the solutions
solutions = []
sol_values = []
sol_weights = []

while done==0:    
    solutionsChecked += 1

    #indices of tabu-unactive members
    tu_ind = np.where(sMem==0)

    #tabu-unactive subset of neighborhood N
    N_star = N[tu_ind]

    #Selecting a candidate
    
    #if all the solutions are tabu:
    if len(N_star)==0:
        all_val = [cf.evaluate(s)[0] for s in N]
        ts.aspiration_criteria(neighborhood=N, values=all_val)
    else:
        #otherwise -
        #Pick the solution with the best value 
        #from non-tabu members even if they are non-improving 
        s_values = [cf.evaluate(s)[0] for s in N_star]
        s = N_star[np.nanargmax(s_values)]
        f_s = cf.evaluate(s)

    #Finding where the flip occurred
    tabu_ind = ts.tabu_criteria(s, x_curr)
    
    #updating all variables
    sMem, sMemVal = ts.st_memory(update_ind = tabu_ind, 
                                 mem = sMem, 
                                 solution = s)

    x_curr = np.copy(s)
    f_curr = np.copy(f_s)

    solutions.append(x_curr)
    sol_values.append(f_curr[0])
    sol_weights.append(f_curr[1])

    N = cf.neighborhood(x_curr)

    #stopping criteria
    counter += 1
    print("iteration: {}, current_solution: {} \n".format(counter, f_curr[0]))
    logger.info("iteration: {}, current_solution: {} \n".format(counter, f_curr[0]))

    if counter == 5:
        done


best_val = np.nanmax(sol_values)
best_weight = sol_weights[np.nanargmax(sol_values)]
best_solution = solutions[np.nanargmax(sol_values)]
    
print ("\n Final number of solutions checked: ", solutionsChecked)
print ("Best value found: ", best_val)
print ("Weight is: ", best_weight)
print ("Total number of items selected: ", np.sum(best_solution))
print ("Best solution: ", best_solution)
