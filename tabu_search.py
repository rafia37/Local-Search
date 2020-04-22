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


    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
