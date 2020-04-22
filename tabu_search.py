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
st_mem = ts.st_memory(init=True)

#initial neighborhood
N = cf.neighborhood(x_curr)



#----------------------
#Tabu Search Algorithm
#----------------------

#A flag to control number of iterations
done = 0

#A counter to count number of iterations
counter = 0

while done==0:

    #tabu-unactive subset of neighborhood N
    tu_ind = ts.tabu_active()       #indices of tabu-unactive members
    N_star = N[]

    #Selecting a candidate solution
    #-----some extended cost func-------
    s = N_star[]
    f_s = cf.evaluate(s)

    #updating
    x_curr = np.copy(s)
    f_curr = np.copy(f_s)

    st_mem = ts.st_memory()

    N = cf.neighborhood(x_curr)

    #stopping criteria
    counter += 1
    print("----- while loop iteration : {} ----- \n".format(counter))
    logger.info("----- while loop iteration : {} ----- \n".format(counter))

    if counter == 5:
        done



    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
