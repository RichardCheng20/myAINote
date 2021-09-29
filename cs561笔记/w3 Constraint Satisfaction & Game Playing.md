#  5 Constraint Satisfaction

## Constraint Satisfaction Problems (CSP) 

 CSPs are a special kind of search problem:

• states defined by values of a fixed set of variables
• goal test defined by constraints on variable values

### 1 Eg: map coloring problem  

定义csp: 1. variables是需要赋值的变量 2.  Domains是变量可以的取值范围 3. Constrains游戏规则

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918121201960.png" alt="image-20210918121201960" style="zoom:50%;" />

 **Assignment:** values are given to some or all variables n 

**Consistent (legal) assignment:** assigned values do not violate any constraint 

**Complete assignment:** every variable is assigned a value 

==Solution== to a CSP: a **consistent and complete** assignment

### Constraint Graph

**Binary CSP:** each constraint relates two variables 

**Constraint Graph:** nodes are variables, arcs are constraints

### Varieties of CSPs

-  Discrete variables 

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918155555564.png" alt="image-20210918155555564" style="zoom:50%;" />

-  Continuous variables

  e.g., start/end times for Hubble Space Telescope observations    / driving 
  n Linear constraints solvable in polynomial time by linear programming

**Constraint Types** 

- **Unary constraints** involve a single variable,		e.g., SA ≠ green
- **Binary constraints** involve pairs of variables,		e.g., SA ≠ WA
- **Higher-order** (sometimes called global) constraints involve 3 or more variables,		eg., cryptarithmetic column constraints

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918160047790.png" alt="image-20210918160047790" style="zoom:50%;" />

Sudoku问题

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918160439990.png" alt="image-20210918160439990" style="zoom:50%;" />

**Solving CSP** Using the “Standard” **Search Approach**

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918160954312.png" alt="image-20210918160954312" style="zoom:50%;" />

## 1 Backtracking search for CSPs

 Backtracking = depth-first search with one variable assigned per node 

- **Variable assignments are commutative**, i.e.,[ WA = red then NT = green ] same as [ NT = green then WA = red ]
- Only need to consider assignments to a ==single variable== at each node --> b = d and there are d^n leaves
- **Depth-first search** for CSPs with **single-variable assignments** is called **backtracking search** 
- Backtracking search is the basic uninformed algorithm for CSPs 
- Can solve n-queens for n≈ 25

**Improving backtracking efficiency**

- Selecting the ==Most Constrained==  **Variable** 即 fewest legal values

   also known as the  **degree heuristic** 先把限制多的分配

  <img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918164009483.png" alt="image-20210918164009483" style="zoom:50%;" />

- Least **constraining value**

the one that rules out the fewest values in the remaining variables

### Node and Arc Consistency

- A  single variable is **node-consistent** if all the values in its domain satisfy the variable’s **unary constraints** 

- A variable is **arc-consistent** if every value in its domain satisfies the binary constraints

  i.e., X~i~ arc-consistent with X~j~ if for every value in D~i~ there exists a value in D~j~ that satisfies the binary constraints on arc (X~i~, X~j~)

- A **network is arc-consistent** if every variable is arc-consistent with every other variable.

 Constraint propagation (e.g., arc consistency) does additional work to constrain values and detect inconsistencies 

**Arc-consistency algorithms:** reduce domains of some variables to achieve network arc-consistency.

#### Arc-consistency

**X -->Y** is consistent iff for ==every== value x of X there is ==some== allowed y

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918170444745.png" alt="image-20210918170444745" style="zoom:50%;" />

不consistency 

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918170645811.png" alt="image-20210918170645811" style="zoom:50%;" />

注意: 

- If X loses a value, neighbors of X need to be rechecked 

- Arc consistency detects failure earlier than forward checking 
- After running AC-3, either **every arc is arc-consistent** or some variable has empty domain, indicating
  the CSP cannot be solved. 
- Can be run as a preprocessor or after each assignment

#### Arc Consistency Algorithm: AC-3

- Start with a queue that contains all arcs
- Pop one arc (X~i~, X~j~) and make X~i~ arc-consistent with respect to X~j~
  • If D~i~ was not changed, continue to next arc,
  • Otherwise, D~i~ was revised (domain was reduced), so need to check all arcs connected to X~i~
  again: add all connected arcs (X~k~, X~i~) to the queue. (this is because the reduction in D~i~ may yield further reductions in D~k~)
  • If D~i~ is revised to empty, then the CSP problem has no solution.

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918172637240.png" alt="image-20210918172637240" style="zoom:50%;" />

## 2 Local search for CSPs

Hill-climbing, simulated annealing typically work with "complete" states, i.e., all variables assigned之前学的局部search方法的变量都已经assigned

- To apply to CSPs:
  • allow states with unsatisfied constraints
  • operators ==reassign== variable values

- Variable selection: randomly select any conflicted variable

- Value selection by min-conflicts heuristic:
  • choose value that violates the **fewest** constraints
  • i.e., hill-climb with h(n) = total number of violated constraints 

**Eg八皇后问题是hill decending**  --> **Min-Conflicts Algorithm**

- States: 4 queens in 4 columns (4 *4 = 256 states) 

- Actions: move queen in column 
- Goal test: no attacks 
-  Evaluation: h(n) = number of attacks 我们希望这个值越小越好

## 06 Game Playing

**Evaluation functions:** heuristics to evaluate utility of a state without exhaustive search

### Two-Player Games

A game formulated as a search problem:

• **Initial state:** board position and turn

• **Operators:** definition of legal moves 

• **Terminal state:** conditions for when game is over

• **Utility function:** a ==numeric== value that describes the **outcome** of the game.  E.g., -1, 0, 1 for loss, draw, win. (AKA  payoff function)

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918181625048.png" alt="image-20210918181625048" style="zoom:33%;" />

### The minimax algorithm

- Perfect play for **deterministic environments** with perfect information

- Basic idea: choose **move with highest minimax value** = best achievable payoff against best play

**Alogrithm:**

1. Generate game tree **completely**

2. Determine utility of each terminal state
3. Propagate the utility values upward in the three by applying MIN and MAX operators
on the nodes in the current level 
4. At the root node use <u>minimax decision</u> to select the move with the max (of the min) utility value

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918213603314.png" alt="image-20210918213603314" style="zoom:50%;" />

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918215638757.png" alt="image-20210918215638757" style="zoom:50%;" />

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918221015788.png" alt="image-20210918221015788" style="zoom:50%;" />

**Evaluation function:** evaluates value of state using heuristics and cuts off search

 **New MINIMAX:**
• **CUTOFF-TEST**: cutoff test to replace the termination condition (e.g., deadline, depth- limit, etc.) 

• EVAL: **evaluation function** to replace utility function (e.g., number of chess pieces taken)

==Note==: Exact Values do not Matter **(Relative Orders are important)**

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918222020520.png" alt="image-20210918222020520" style="zoom:50%;" />

==Reduce Search==: $\alpha+\beta$  pruning for search cutoff

 **$\alpha+\beta$  pruning:** the basic idea is to prune portions of the search tree that cannot improve the utility value of the max or min node, by just considering the values of nodes seen so far.



### Resource limitations



### alpha-beta pruning

一定能找到optimal solution

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918230346884.png" alt="image-20210918230346884" style="zoom:50%;" />

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918230524805.png" alt="image-20210918230524805" style="zoom:50%;" />

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918231633353.png" alt="image-20210918231633353" style="zoom:50%;" />

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210918231827684.png" alt="image-20210918231827684" style="zoom:50%;" />

- $\alpha$: Best choice so far for MAX • 

- $\beta$: Best choice so far for MIN

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210919083545477.png" alt="image-20210919083545477" style="zoom:50%;" />





### Nondeterministic games/Elements of chance

求期望即可

但是value有影响

<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210919084707787.png" alt="image-20210919084707787" style="zoom:50%;" />



## Discussion

For Search, you can represent your desires as the objective function
• Choice 1: *x as a state*, F(x) as the “rewards” of states
• Choice 2: *x as a path*, F(x) as the “rewards” of paths
• Degree of “goodness”: goal related, cost related, etc.



**Hill climbing**
• Idea: Use local gradient(x) to determine direction, always heads to the better
• Pros: simple, local, incremental, no memory
• Cons: may be trapped in local extreme Simulated Annealing

**Simulated Annealing**

• Ideas: long and random jumps when temperature is high
• Pros: may avoid local extreme
• Cons: expensive, not always find x*, 



<img src="w3%20Constraint%20Satisfaction%20&%20Game%20Playing.assets/image-20210919105822381.png" alt="image-20210919105822381" style="zoom:50%;" />





