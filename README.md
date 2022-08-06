# Applying Dynamic Programming for Job Scheduling Problem

## Problem

Suppose you have one machine and a set of $n$ jobs $a_1, a_2, ..., a_n$ to process on that machine. 
Each job $a_j$ has a processing time $t_j$ , a profit $p_j$ and a deadline $d_j$ . The machine can only do
one job at a time, and job $a_j$ must run uninterruptedly for $t_j$ consecutive time units. If 
job $a_j$ is completed by its deadline $d_j$, you receive a profit $p_j$, but if it’s completed after 
its deadline, you receive a profit of $0$. Give a dynamic programming algorithm to find the 
schedule that obtains the maximum amount of profit, assuming that all processing times are 
integers between $1$ and $n$.

## Solution
### Step 1 Characterize the structure of the optimal solution

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

Where $𝑘$ is the job that is currently being added to the schedule, and elements in $𝑆$ refers to each
combination of jobs that have been already processed. $𝑡_𝑖$ is the processing time of each job, and $h_𝑘$ 
is the function that determines if profit $𝑝_𝑘$ takes the value of $𝑝_𝑘$ or 0. In other words, $h_𝑘$ defines if profit $𝑝_𝑘$ 
remains with its original value (considering that the total processing time is completed by the deadline $𝑑_𝑘$), 
or if it turns to $0$, (considering that the total processing time is not completed by the deadline $𝑑_𝑘$).

### Step 2 Recursively define the value of an optimal solution
Next, we obtained the recurrence relation, where if the size of the problem $𝑛$ is equal to $1$, we would only have 
one way of scheduling the jobs (e.g., $𝑝_1$). However, if we have a size problem of $𝑛 \geq 2$ the recursive solution would be:

$$ 
f[S] =
\begin{cases}
max\Big[f\[i\]+h_k\big(\sum_{\forall i \in S}{t_i}\big)\Big]  & \quad \forall i \in C, \text{if } n \geq 2\\
p_1 & \quad \text{if } n = 1
\end{cases}
$$

Where $𝐶$ are the possible combinations, considering that $𝑙𝑒𝑛𝑔𝑡h(𝑆)$ elements have been scheduled
and $a_𝑘$ is currently being added. For example, if we want to add $𝑎_1$, then $𝑘 = 1$, and $𝑓[𝐶]$ would be equal to $𝑓[𝑎_2, 𝑎_3]$. 
This happens because, we would add 
the profit of scheduling $𝑎_1$ to the already obtained profit of scheduling $𝑎_2$ and $𝑎_3$. Thus, the number of
possible combinations $𝐶$ is equal to $\binom{S}{d}$ (where $𝑑=𝑙𝑒𝑛𝑔𝑡h(𝑠) − 1$).

In addition, the maximum number of combinations $C$ is equal to $\binom{n}{l}$, where $𝑙$ is the current iteration number. 
For example, if we have a size problem $𝑛 = 4$ and we are developing the first iteration $𝑙 = 1$, then the number of combinations $C$
would be $\binom{4}{1}=4$ ( $𝑆=\[𝑠_1, 𝑠_2, 𝑠_3, 𝑠_4\]$). Where $s_1 = 𝑎_1$, $𝑠_2 =𝑎_2$, $𝑠_3 =𝑎_3$, $𝑠_4 =𝑎_4$. Hence the evaluations 
done are for: $𝑓\[𝑎_1\]$, $𝑓\[𝑎_2\]$, $𝑓\[𝑎_3\]$, and $𝑓\[𝑎_4\]$.
To illustrate this better we will follow up in the case where we have developed the second iteration, where $𝑙 = 2$ and so the number of 
evaluations is $\binom{4}{2}=6$. This would result in the following evaluations
following form: $𝑓\[𝑎_1,𝑎_2\]$, $𝑓\[𝑎_1,𝑎_3\]$, $𝑓\[𝑎_1,𝑎_4\]$, $𝑓\[𝑎_2,𝑎_3\]$, $𝑓\[𝑎_2,𝑎_4\]$, and $𝑓\[𝑎_3,𝑎_4\]$.

### Step 3 Calculate the value of the optimal solution in a bottom-up way
Now we provide the solution for the problem, considering that we have the following data:

Job (j) | Processing time ($t_j$) | Deadline ($d_j$) | Profit ($p_j$) |
--- | --- | --- | --- |
1 | 4 | 10 | 2 | 
2 | 4 | 15 | 5 | 
3 | 5 | 5 | 3 | 
4 | 6 | 10 | 4 | 

#### First Iteration
$𝑓_1[𝑎_1]= 2 \quad\quad\quad\quad 𝑘[1] = 1$ <br />
$𝑓_1[𝑎_2]= 5 \quad\quad\quad\quad 𝑘[2] = 2$ <br />
$𝑓_1[𝑎_3]= 3 \quad\quad\quad\quad 𝑘[3] = 3$ <br />
$𝑓_1[𝑎_4]= 4 \quad\quad\quad\quad 𝑘[4] = 4$

#### Second Iteration
$𝑓_2[𝑎_1,a_2]= max \big[f_1\[a_1\]+h_2\(t_1+t_2\), f_1\[a_2\]+h_1\(t_1+t_2\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+5,5+2\big]$ <br />
$\quad\quad\quad\quad =max\big[7,7\big]$ <br />
$\quad\quad\quad\quad =7$<br />
$\quad k\[1,2\] = 1,2$<br />
<br />
$𝑓_2[𝑎_1,a_3]= max \big[f_1\[a_1\]+h_3\(t_1+t_3\), f_1\[a_3\]+h_1\(t_1+t_3\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+0,3+2\big]$ <br />
$\quad\quad\quad\quad =max\big[2,5\big]$ <br />
$\quad\quad\quad\quad =5$<br />
$\quad k\[1,3\] = 1$<br />
<br />
$𝑓_2[𝑎_1,a_4]= max \big[f_1\[a_1\]+h_4\(t_1+t_4\), f_1\[a_4\]+h_1\(t_1+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[2+4,4+2\big]$ <br />
$\quad\quad\quad\quad =max\big[6,6\big]$ <br />
$\quad\quad\quad\quad =6$<br />
$\quad k\[1,4\] = 1,4$<br />
<br />
$𝑓_2[𝑎_2,a_3]= max \big[f_1\[a_2\]+h_3\(t_2+t_3\), f_1\[a_3\]+h_2\(t_2+t_3\)\big]$ <br />
$\quad\quad\quad\quad =max\big[5+0,3+5\big]$ <br />
$\quad\quad\quad\quad =max\big[5,8\big]$ <br />
$\quad\quad\quad\quad =8$<br />
$\quad k\[2,3\] = 2$<br />
<br />
$𝑓_2[𝑎_2,a_4]= max \big[f_1\[a_2\]+h_4\(t_2+t_4\), f_1\[a_4\]+h_2\(t_2+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[5+4,4+5\big]$ <br />
$\quad\quad\quad\quad =max\big[9,9\big]$ <br />
$\quad\quad\quad\quad =9$<br />
$\quad k\[2,4\] = 2,4 $<br />
<br />
$𝑓_2[𝑎_3,a_4]= max \big[f_1\[a_3\]+h_4\(t_3+t_4\), f_1\[a_4\]+h_3\(t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad =max\big[3+0,4+0\big]$ <br />
$\quad\quad\quad\quad =max\big[3,4\big]$ <br />
$\quad\quad\quad\quad =4$<br />
$\quad k\[3,4\] = 3 $<br />
<br />

#### Third Iteration
$𝑓_3[𝑎_1,a_2,a_3]= max \big[f_2\[a_1,a_2\]+h_3\(t_1+t_2+t_3\), f_2\[a_1,a_3\]+h_2\(t_1+t_2+t_3\), f_2\[a_2,a_3\]+h_1\(t_1+t_2+t_3\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7+0,5+5,8+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7,10,8\big]$ <br />
$\quad\quad\quad\quad\quad\quad =10$<br />
$\quad\quad k\[1,2,3\] = 2$<br />
<br />
$𝑓_3[𝑎_1,a_2,a_4]= max \big[f_2\[a_1,a_2\]+h_3\(t_1+t_2+t_4\), f_2\[a_1,a_4\]+h_2\(t_1+t_2+t_4\), f_2\[a_2,a_4\]+h_1\(t_1+t_2+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7+0,6+5,9+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[7,11,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =11$<br />
$\quad\quad k\[1,2,4\] = 2$<br />
<br />
$𝑓_3[𝑎_1,a_3,a_4]= max \big[f_2\[a_1,a_3\]+h_3\(t_1+t_3+t_4\), f_2\[a_1,a_4\]+h_3\(t_1+t_3+t_4\), f_2\[a_3,a_4\]+h_1\(t_1+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5+0,6+0,4+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5,6,4\big]$ <br />
$\quad\quad\quad\quad\quad\quad =6$<br />
$\quad\quad k\[1,3,4\] = 3$<br />
<br />
$𝑓_3[𝑎_2,a_3,a_4]= max \big[f_2\[a_2,a_3\]+h_3\(t_2+t_3+t_4\), f_2\[a_2,a_4\]+h_3\(t_2+t_3+t_4\), f_2\[a_3,a_4\]+h_2\(t_2+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[8+0,9+0,4+5\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[5,9,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =9$<br />
$\quad\quad k\[2,3,4\] = 2,3$<br />
<br />

#### Fourth Iteration
$𝑓_4[𝑎_1,a_2,a_3,a_4]= max \big[f_3\[𝑎_1,a_2,a_3\]+h_4\(t_1+t_2+t_3+t_4\), f_3\[𝑎_1,a_2,a_4\]+h_3\(t_1+t_2+t_3+t_4\), f_3\[𝑎_1,a_3,a_4\]+$ <br />
$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad h_2\(t_1+t_2+t_3+t_4\), f_1\[a_2,a_3,a_4\]+h_4\(t_1+t_2+t_3+t_4\)\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[10+0,11+0,6+0,9+0\big]$ <br />
$\quad\quad\quad\quad\quad\quad =max\big[10,11,6,9\big]$ <br />
$\quad\quad\quad\quad\quad\quad =11$<br />
$\quad\quad k\[1,2,3,4\] = 3$<br />
<br />

# Solution 
1 --> 4 --> 2 --> 3
