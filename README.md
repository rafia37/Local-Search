# Local-Search
In this repository, I implement several heuristic and metaheuristic algorithms to
solve a random instance of the knapsack problem. In this particular instance of the
problem, I used 150 items to choose from and a maximum weight limit of 1500 kg
for the knapsack. The objective is to maximize the total value in the knapsack.
The weights and values of each item is randomly generated using Python's `random`
library.

The algorithms I implement are -

1. Neighborhood-Based Heuristics
	- Hill Climbing and variations (HC)
		- Steepest ascent
		- First accept
		- Random restarts
		- Random walk
		- Local beam search
		- Stochastic beam search
	- Simulated Annealing (SA)
	- Variable Neighborhood Search (VNS)
		- Using variable neighborhhod descent (VND)
		- Using HC with steepest ascent
		- Implementing reduced variable neighborhood search (RVNS)
	- Tabu Search (TS)
		- Implementing long-term memory
		- Implementing path relinking
	- Guided Local Search
2. Population-Based Metaheuristics
	- Genetic Algorithm (GA)
	- Particle Swarm Optimization (PSO)

This readme page is under construction and I have not implemented every
algorithm yet. So here is an incomplete table of results -

| Algorithm | Iteration | Time | Items | Weight | Objective |
| --------- | --------- | ---- | ----- | ------ | --------- |
| HC steepest ascent | 1050 | 0000 | 15 | 1496.39 | 12915.9 |
| HC first accept | 230 | 0000 | 17 | 1495.50 | 11368.6 |
| HC random restarts | 223650 | 0000 | 18 | 1489.00 | 14475.6 |
| HC random walk | 604 | 0000 | 16 | 1495.69 | 12997.0 |
| HC local beam search | 0000 | 0000 | 0000 | 0000 | 0000 |
| HC stochastic beam search | 0000 | 0000 | 0000 | 0000 | 0000 |
| Simulated Annealing | 26500 | 0000 | 29 | 1498.80 | 16744.4 |
| VNS using VND | 1802 | 0000 | 31 | 1499.80 | 19442.6 |
| VNS using HC | 0000 | 0000 | 0000 | 0000 | 0000 |
| RVNS | 0000 | 0000 | 0000 | 0000 | 0000 |
| Tabu Search (basic) | 200 | 0000 | 21 | 1498.40 | 16049.5 |
| TS using long-term memory | 0000 | 0000 | 0000 | 0000 | 0000 |
| TS using path relinking | 0000 | 0000 | 0000 | 0000 | 0000 |
| Genetic Algorithm | 0000 | 0000 | 0000 | 0000 | 0000 |
| Particle Swarm Optimization | 0000 | 0000 | 0000 | 0000 | 0000 |

In the table above, *Algorithm* column is name of the algorithm, *Iteration*
column is the number of iterations it took to find the solution, *Time* column is
the program running time in seconds, *Items* column is the number of items chosen
in the optimal solution, *Weight* column is the total weight in kg of the
knapsack after choosing the items in optimal solution and finally, the *Objective*
column is the total value in dollar of all the items selected in optimal solution,
i.e. the quantity we're trying to maximize in this problem.
