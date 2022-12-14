# Applying Dynamic Programming for Job Scheduling Problem

## Problem

Suppose you have one machine and a set of $n$ jobs $a_1, a_2, ..., a_n$ to process on that machine. 
Each job $a_j$ has a processing time $t_j$ , a profit $p_j$ and a deadline $d_j$ . The machine can only do
one job at a time, and job $a_j$ must run uninterruptedly for $t_j$ consecutive time units. If 
job $a_j$ is completed by its deadline $d_j$, you receive a profit $p_j$, but if itβs completed after 
its deadline, you receive a profit of $0$. Give a dynamic programming algorithm to find the 
schedule that obtains the maximum amount of profit, assuming that all processing times are 
integers between $1$ and $n$.

## Solution
<!---### Step 1 Characterize the structure of the optimal solution

We obtain the profit when adding a job into the sequence, using the following equation:

$$ h_k\big(\sum_{\forall i \in S}{t_i}+t_k\big)=\sum_{\forall i \in S}{p_i}+p_k$$

where $h_k$ is a function that defines if:

$$
p_k =
  \begin{cases}
    p_k       & \quad \text{if } \sum_{\forall i \in S}{t_i}+t_k \leq d_k\\
    0  & \quad \text{if } \sum_{\forall i \in S}{t_i}+t_k > d_k\\
  \end{cases}
$$

Where $π$ is the job that is currently being added to the schedule, and elements in $π$ refers to each
combination of jobs that have been already processed. $π‘_π$ is the processing time of each job, and $h_π$ 
is the function that determines if profit $π_π$ takes the value of $π_π$ or 0. In other words, $h_π$ defines if profit $π_π$ 
remains with its original value (considering that the total processing time is completed by the deadline $π_π$), 
or if it turns to $0$, (considering that the total processing time is not completed by the deadline $π_π$).

### Step 2 Recursively define the value of an optimal solution
Next, we obtained the recurrence relation, where if the size of the problem $π$ is equal to $1$, we would only have 
one way of scheduling the jobs (e.g., $π_1$). However, if we have a size problem of $π \geq 2$ the recursive solution would be:

$$ 
f[S] =
\begin{cases}
max\Big[f\[i\]+h_k\big(\sum_{\forall i \in S}{t_i}\big)\Big]  & \quad \forall i \in C, \text{if } n \geq 2\\
p_1 & \quad \text{if } n = 1
\end{cases}
$$

Where $πΆ$ are the possible combinations, considering that $πππππ‘h(π)$ elements have been scheduled
and $a_π$ is currently being added. For example, if we want to add $π_1$ and $C=π_2, π_3, then $π = 1$, and $π[πΆ]$ would be equal to $π[π_2, π_3]$. 
This happens because, we would add the profit of scheduling $π_1$ to the already obtained profit of scheduling $π_2$ and $π_3$. Thus, the number of
possible combinations $πΆ$ is equal to $\binom{S}{d}$ (where $π=πππππ‘h(π ) β 1$).

In addition, the maximum number of combinations $C$ is equal to $\binom{n}{l}$, where $π$ is the current iteration number. 
For example, if we have a size problem $π = 4$ and we are developing the first iteration $π = 1$, then the number of combinations $C$
would be $\binom{4}{1}=4$ ( $π=\[π _1, π _2, π _3, π _4\]$). Where $s_1 = π_1$, $π _2 =π_2$, $π _3 =π_3$, $π _4 =π_4$. Hence the evaluations 
done are for: $π\[π_1\]$, $π\[π_2\]$, $π\[π_3\]$, and $π\[π_4\]$.
To illustrate this better we will follow up in the case where we have developed the second iteration, where $π = 2$ and so the number of 
evaluations is $\binom{4}{2}=6$. This would result in the following evaluations
following form: $π\[π_1,π_2\]$, $π\[π_1,π_3\]$, $π\[π_1,π_4\]$, $π\[π_2,π_3\]$, $π\[π_2,π_4\]$, and $π\[π_3,π_4\]$.

### Step 3 Calculate the value of the optimal solution in a bottom-up way-->
Now we provide the solution for the problem, considering that we have the following data:

Job (j) | Processing time ($t_j$) | Deadline ($d_j$) | Profit ($p_j$) |
--- | --- | --- | --- |
1 | 4 | 10 | 2 | 
2 | 4 | 15 | 5 | 
3 | 5 | 5 | 3 | 
4 | 6 | 10 | 4 | 

#### First Iteration
$π_1[π_1]= 2 \quad\quad\quad\quad π[1] = 1$ <br />
$π_1[π_2]= 5 \quad\quad\quad\quad π[2] = 2$ <br />
$π_1[π_3]= 3 \quad\quad\quad\quad π[3] = 3$ <br />
$π_1[π_4]= 4 \quad\quad\quad\quad π[4] = 4$

#### Second Iteration
$π_2[π_1,a_2]= max \big[f_1\[a_1\]+h_2\(t_1+t_2\), f_1\[a_2\]+h_1\(t_1+t_2\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+5,5+2\big]$ <br />
$\quad\quad\quad\quad =max\big[7,7\big]$ <br />
$\quad\quad\quad\quad =7$<br />
$\quad k\[1,2\] = 1,2$<br />
<br />
$π_2[π_1,a_3]= max \big[f_1\[a_1\]+h_3\(t_1+t_3\), f_1\[a_3\]+h_1\(t_1+t_3\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+0,3+2\big]$ <br />
$\quad\quad\quad\quad =max\big[2,5\big]$ <br />
$\quad\quad\quad\quad =5$<br />
$\quad k\[1,3\] = 1$<br />
<br />
$π_2[π_1,a_4]= max \big[f_1\[a_1\]+h_4\(t_1+t_4\), f_1\[a_4\]+h_1\(t_1+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+4,4+2\big]$ <br />
$\quad\quad\quad\quad =max\big[6,6\big]$ <br />
$\quad\quad\quad\quad =6$<br />
$\quad k\[1,4\] = 1,4$<br />
<br />
$π_2[π_2,a_3]= max \big[f_1\[a_2\]+h_3\(t_2+t_3\), f_1\[a_3\]+h_2\(t_2+t_3\)\big]$ <br />
$\quad\quad\quad\quad =max\big[5+0,3+5\big]$ <br />
$\quad\quad\quad\quad =max\big[5,8\big]$ <br />
$\quad\quad\quad\quad =8$<br />
$\quad k\[2,3\] = 2$<br />
<br />
$π_2[π_2,a_4]= max \big[f_1\[a_2\]+h_4\(t_2+t_4\), f_1\[a_4\]+h_2\(t_2+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[5+4,4+5\big]$ <br />
$\quad\quad\quad\quad =max\big[9,9\big]$ <br />
$\quad\quad\quad\quad =9$<br />
$\quad k\[2,4\] = 2,4 $<br />
<br />
$π_2[π_3,a_4]= max \big[f_1\[a_3\]+h_4\(t_3+t_4\), f_1\[a_4\]+h_3\(t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[3+0,4+0\big]$ <br />
$\quad\quad\quad\quad =max\big[3,4\big]$ <br />
$\quad\quad\quad\quad =4$<br />
$\quad k\[3,4\] = 3 $<br />
<br />

#### Third Iteration
$π_3[π_1,a_2,a_3]= max \big[f_2\[a_1,a_2\]+h_3\(t_1+t_2+t_3\), f_2\[a_1,a_3\]+h_2\(t_1+t_2+t_3\), f_2\[a_2,a_3\]+h_1\(t_1+t_2+t_3\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7+0,5+5,8+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7,10,8\big]$ <br />
$\quad\quad\quad\quad\quad\quad =10$<br />
$\quad\quad k\[1,2,3\] = 2$<br />
<br />
$π_3[π_1,a_2,a_4]= max \big[f_2\[a_1,a_2\]+h_3\(t_1+t_2+t_4\), f_2\[a_1,a_4\]+h_2\(t_1+t_2+t_4\), f_2\[a_2,a_4\]+h_1\(t_1+t_2+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7+0,6+5,9+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7,11,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =11$<br />
$\quad\quad k\[1,2,4\] = 2$<br />
<br />
$π_3[π_1,a_3,a_4]= max \big[f_2\[a_1,a_3\]+h_3\(t_1+t_3+t_4\), f_2\[a_1,a_4\]+h_3\(t_1+t_3+t_4\), f_2\[a_3,a_4\]+h_1\(t_1+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5+0,6+0,4+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5,6,4\big]$ <br />
$\quad\quad\quad\quad\quad\quad =6$<br />
$\quad\quad k\[1,3,4\] = 3$<br />
<br />
$π_3[π_2,a_3,a_4]= max \big[f_2\[a_2,a_3\]+h_3\(t_2+t_3+t_4\), f_2\[a_2,a_4\]+h_3\(t_2+t_3+t_4\), f_2\[a_3,a_4\]+h_2\(t_2+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[8+0,9+0,4+5\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5,9,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =9$<br />
$\quad\quad k\[2,3,4\] = 2,3$<br />
<br />

#### Fourth Iteration
$π_4[π_1,a_2,a_3,a_4]= max \big[f_3\[π_1,a_2,a_3\]+h_4\(t_1+t_2+t_3+t_4\), f_3\[π_1,a_2,a_4\]+h_3\(t_1+t_2+t_3+t_4\), f_3\[π_1,a_3,a_4\]+$ <br />
$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad h_2\(t_1+t_2+t_3+t_4\), f_1\[a_2,a_3,a_4\]+h_4\(t_1+t_2+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[10+0,11+0,6+0,9+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[10,11,6,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =11$<br />
$\quad\quad k\[1,2,3,4\] = 3$<br />
<br />

# Solution 
1 --> 4 --> 2 --> 3
