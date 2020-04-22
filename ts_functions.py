#Functions used by Tabu Search

import numpy as np
import problem_instance as pi


def tabu_criteria(new_solution, old_solution):

    #find the index where flip occurred
    temp = np.where(new_solution!=old_solution)[0]
    
    if len(temp)>1:
        print("WARNING found more than one flip")

    ind = temp[0]

    return ind


def aspiration_criteria():
    return

#Short term memory
def st_memory(update_ind, tenure = 3, init = False, mem = 0):

    #if memory is to be initialized, set every element to 0
    if init:
        mem = np.zeros(pi.n, dtype=int)
    else:       #else update memory
        #if memory is to be updated but old memory is not provided, raise error
        if type(mem)==int:
            print("Need to provide old memory if you want to update memory \n")
            print("Old memory needs to be an array of size n \n")
            raise TypeError
        
        #update every active element score
        for i, m in enumerate(mem):
            if m>0:
                mem[i] -= 1

        #update memory with new active element
        mem[update_ind] = tenure    

    return mem



#Long term memory
def lt_memory():
    return

def path_relinking():
    return