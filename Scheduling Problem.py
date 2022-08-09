#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Import libraries
import math
from itertools import combinations


# In[22]:


# A is the number reference of the job (the field should be filled with sequenced numbers starting by 1)
A = [1   , 2  , 3  , 4  ]
# T is the processing time of each job
T = [4   , 4  , 5  , 6  ]
# D is the deadline in which each job must be completed 
# (D should always be higher or equal to T)
D = [10  , 15 , 5  , 10 ]
# P is the profit if the job is completed before its deadline
P = [2   , 5  , 3  , 4  ]
# n is the number of jobs
n = len(A)


# In[23]:


# get the total processing time
def Completion(job):
    E = 0
    for k in job:
        E = E + T[k-1]
    return E


# In[24]:


# adds the profit of the job if they are completed before their deadline
def Profit(all_jobs,completion_time,current_job):
    if completion_time>D[current_job[0]-1]:
        profit = 0
    else:
        profit = P[current_job[0]-1]
        
    return profit


# In[25]:


# This function obtains the maximum profit according to the information given of each job
def scheduling():
    c={}
    r={}
    p={}
    for i in range(n):
        # generate all possible combinations of size n with the given jobs
        # (i.e., [(1,), (2,), (3,), (4,)], 
        #        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        #        [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        #        [(1, 2, 3, 4)])
        comb = (list(combinations(A,i+1)))
        
        # get the total profit of each combination of jobs
        for j in comb:
            # first get the total processing time of each combination of jobs
            c[j]=Completion(j)
            
            if len(j)==1:
                # if the length of the combination is equal to 1 then the profit of this would be equal 
                # to the job's individual profit (i.e., if j=(1,) then p[j]=2)
                p[j]=(P[j[0]-1])
            else:
                # if the length of the combination is higher than 1, (i.e., j=(1, 2) or j=(1, 2, 4)) this means  
                # that we need to evaluate if the processing time of these jobs meets the deadline and add the  
                # profit accordingly.
            
                # create a new set of combinations of size len(j)-1 with the j jobs 
                # (i.e., if j=(1, 2) then comb2=[(1,), (2,)]
                #        if j=(1, 2, 4) then comb2=[(1, 2), (1, 4), (2, 4)])
                comb2 = (list(combinations(j,len(j)-1)))
                current_profit = []
                route = []
                
                # We are going to obtain the profit when adding each element to each combination k in 
                # comb2 (i.e., if k = (1, 2) then the job that would be added is 4. Next, we obtain the profit 
                # when jobs (1, 2) have already been processed. Finally, the profit of processing job 4
                # is added considering if the total processing time meets the deadline of not.)
                for k in comb2:
                    #
                    current_job = (list(set(j) - set(k)))
                    route.append(current_job[0])
                    past_jobs = (list(set(k)))
                    past_profit = p[k]
                    additional_profit = Profit(j,c[j],current_job)
                    current_profit.append(additional_profit+past_profit)
                
                # We obtain the combination of jobs with maximum profit 
                max_index = current_profit.index(max(current_profit))
                p[j]=current_profit[max_index]
                r[j]=route[max_index]
                current_profit = []
                route = []

    return p[tuple(A)],r
            
            


# In[26]:


# get the sequence in which the jobs should be ordered to obtain the maximum profit
def job_accomodation(route):
    x = A
    k = route[tuple(A)]
    final_route = [k]
    for i in range(len(A)-2):
        x = list(filter((k).__ne__, x))
        k = route[tuple(x)]
        final_route.append(k)
    final_route.append(list(set(A) - set(final_route))[0])
    return(final_route)


# In[27]:


max_profit, routes = scheduling()
print("profit: ",max_profit)
print("scheduling: ",job_accomodation(routes))

