#Hil climbing with best improvement (steepest ascent)
#author: Charles Nicholson

#Student name: Rafia Bushra
#Date: 4/5/2020



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
        #print ("Found an infeasible solution")   
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




#varaible to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution()  #x_curr will hold the current solution 
x_best = np.copy(x_curr)     #x_best will hold the best solution 
f_curr = evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
f_best = np.copy(f_curr)


#begin local search overall logic ----------------
done = 0
    
while done == 0:
        
    Neighborhood = neighborhood(x_curr)   #create a list of all neighbors in the neighborhood of x_curr
    
    for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        
        #Handling infeasible solution
        try:
            eval_s = evaluate(s)
        except:
            #print("Infeasible solution handled")
            continue
        
        if eval_s[0] > f_best[0]: 
            x_best = np.copy(s)                 #find the best member and keep track of that solution
            f_best = np.copy(eval_s)       #and store its evaluation  
    
    if list(f_best) == list(f_curr):               #if there were no improving solutions in the neighborhood
        done = 1
    else:
        x_curr = np.copy(x_best)         #else: move to the neighbor solution and continue
        f_curr = np.copy(f_best)         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_best)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
