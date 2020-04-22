#Functions used by Tabu Search

import numpy as np
import problem_instance as pi


def tabu_criteria():
    return

def tabu_tenure():
    return

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

mem1 = np.zeros(pi.n, dtype=int)
mem1[3] = 3
mem1[5] = 2
mem1[7] = 1
print(st_memory(0, mem=mem1))

#Long term memory
def lt_memory():
    return

def path_relinking():
    return