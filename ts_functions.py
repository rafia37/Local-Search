#Functions used by Tabu Search

import numpy as np
import problem_instance as pi



def tabu_criteria(new_solution, old_solution):

    #find the index where flip occurred
    ind = np.where(new_solution!=old_solution)[0]
    
    if len(ind)>1:
        print("WARNING found more than one flip")

    return ind[0]



def aspiration_criteria(curr_value=0, val_history=[], neighborhood = [], values=[]):

    #If a neighborhood is provided (which means all solutions are tabu)
    #pick the best solution
    if len(neighborhood) > 0:
        sol = neighborhood[np.nanargmax(values)]
        return sol

    else:   
        #if the current solution is higher than the best found so far
        #accept it even if it's tabu
        max_val_so_far = np.nanmax(np.array(val_history))
        accept = 0
        if curr_val > max_val_so_far:
            accept = 1

        return accept



def tabu_active(sMem, sMemVal, Neighborhood):

    #indices of tabu active elements
    active_ind = np.where(sMem>0)[0]
    
    #A list to hold the tabu unactive neighbors
    newN = []

    #A loop to check whether each solution is tabu active or not
    for N in Neighborhood:

        #A flag to represent the tabu active status of an element
        not_tabu_active = 1

        for i, a in enumerate(active_ind):
            #If there is even one tabu_active member -
            #do not include this solution and,
            #break out of this loop as soon as you find the first tabu active element
            if (N[a] == sMemVal[a]):
                not_tabu_active = 0
                break
        #If there are no tabu active members, add this solution
        if not_tabu_active:
            newN.append(N)

    return np.array(newN)




#Short term memory
def st_memory(update_ind, tenure = 3, init = False, mem = 0, solution = 0):
    """
        update_ind: index of the element that was flipped
        solution: this is the candidate solution. we want the flipped value
    """

    #if memory is to be initialized, set every element to 0
    if init:
        mem = np.zeros(pi.n, dtype=int)
        memValue = np.array([2]*pi.n)

    else:       #else update memory
        #if memory is to be updated but old memory is not provided, raise error
        if (type(mem)==int) | (type(solution)==int):
            print("Need to provide old memory and solution if you want to update memory \n")
            print("Old memory and solution needs to be an array of size n \n")
            raise TypeError
        
        #update every active element score
        for i, m in enumerate(mem):
            if m>0:
                mem[i] -= 1
                if mem[i] == 0:
                    memValue[i] = 2

        #update memory with new active element
        mem[update_ind] = tenure 
        memValue[update_ind] = solution[update_ind]

    return mem, memValue



#Long term memory
def lt_memory():
    return

def path_relinking():
    return