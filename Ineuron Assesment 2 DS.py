#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question: 2
#Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of horses that are mad. To prevent the horses from hurting each other, you need to assign the horses to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.
#array: 1,2,4,8,9  &  k=3
#O/P: 3
#Explanation: 1st horse at stall 1, 2nd horse at stall 4 and 3rd horse at stall 8

def count_horses(stalls, distance):
    count = 1
    last_position = stalls[0]
    for stall in stalls:
        if stall - last_position >= distance:
            count += 1
            last_position = stall
    return count
def largest_minimum_distance(stalls, k):
    stalls.sort()
    left = 1
    right = stalls[-1] - stalls[0] + 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if count_horses(stalls, mid) >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
arr = [1, 2, 4, 8, 9]
k = 3
print(largest_minimum_distance(arr, k))  


# In[5]:


# Question 4
#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
   #a) 0 <= a, b, c, d < n
   #b) a, b, c, and d are distinct.
   #c) nums[a] + nums[b] + nums[c] + nums[d] == target



def four_sum(nums, target):
    nums.sort()
    quadruplets = []
    n = len(nums)
    
    for a in range(n - 3):
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplets.append([nums[a], nums[b], nums[c], nums[d]])
    
    return quadruplets
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))


# In[ ]:


#Question: 1
#Given the following tables:
#What will be the result of the query below?
#SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races)
#Explain your answer and also provide an alternative version of this query that will avoid the issue that it exposes.
Select * FROM  runners where 
id <> 2 and 
id <> 3 and 
id <> null ;

SELECT runners*
FROM runners 
LEFT JOIN  races on runners.id = races.winner_id
WHERE races.winner_id IS NULL;


# In[ ]:


#Question: 2
#Given two tables created as follows
#Write a query to fetch values in table test_a that are and not in test_b without using the NOT keyword.
select * from test_a
except
select * from test_b


# In[ ]:


#Question: 3
#Given the following tables:
#Write a query to to get the list of users who took the a training lesson more than once in the same day, grouped by user and training lesson, each ordered from the most recent lesson date to oldest date.
SELECT u.username, td.training_id, td.training_date
fROM users u
JOIN training_details td ON u.user_id = td.user_id
GROUP BY u.user_id, td.training_id, td.training_date
Having COUNT(*)>1
ORDER BY td.training_date DESC;


# In[ ]:


#Question: 4Consider the Employee table below.

SELECT E2.EMP_ID, E2.EMP_NAME, AVG(E1.SALARY)
FROM MANAGER_EMP E1
INNER JOIN MANAGER_EMP E2
ON E1.MANAGER_ID = E2.EMP_ID
GROUP BY E2.EMP_ID. E2.EMP_NAME


# #Question: 1
# #What is the meaning of six sigma in statistics?  Give proper example
# Six sigma is statistics concept and methodology that improve the quality of process outputs by identifying and removing the causes of defects and minimizing variables. 
# The term "Six Sigma" refers to a level of quality that results in only 3.4 defects per million opportunities (DPMO). It signifies a high level of process capability and consistency.
# 
# The 5 Steps of Six Sigma
# Define
# A team of people, led by a Six Sigma expert, chooses a process to focus on and defines the problem it wishes to solve.
# Measure
# The team measures the initial performance of the process, creating a benchmark, and pinpoints a list of inputs that may be hindering performance.
# Analyze
# Next the team analyzes the process by isolating each input, or potential reason for any failures, and testing it as the possible root of the problem.
# Improve
# The team works from there to implement changes that will improve system performance.
# Control
# The group adds controls to the process to ensure it does not regress and become ineffective once again.
# 
# 

# #Question: 2
# #What type of data does not have a log-normal distribution or a Gaussian distribution?  Give proper example
# Exponential distributions do not have a log-normal distribution or a Gaussian distribution. In fact, any type of data that is categorical will not have these distributions as well.
# Example: Duration of a phone car, time until the next earthquake, etc.
# 
# Data that do not have a log-normal distribution or a Gaussian (normal) distribution are typically those that exhibit non-symmetric or skewed distributions. Some examples of data that do not follow a log-normal or Gaussian distribution include:
# Poisson distributed data
# Exponential distributed data
# Uniformly distributed data
# Skewed data
# These are just a few examples of data distributions that do not follow a log-normal or Gaussian distribution. 
# 

# Question: 3
# What is the meaning of the five-number summary in Statistics? Give proper example
# 
# The five number summary includes 5 items: The minimum. Q1 (the first quartile, or the 25% mark). The median. Q3 (the third quartile, or the 75% mark). The maximum. The five number summary gives you a rough idea about what your data set looks like. for example, you’ll have your lowest value (the minimum) and the highest value (the maximum).
# 
# The minimum.
# Q1 (the first quartile, or the 25% mark).
# The median.
# Q3 (the third quartile, or the 75% mark).
# The maximum
# 
# Minimum: The smallest value in the dataset. 
# 
# Q1(First Quartile) : The value below which 25% of the data falls. It is also the median of the lower half of the dataset.
# 
# Median (Q2): The middle value of the dataset when it is ordered from least to greatest. It divides the dataset into two equal halves.
# 
# Q3 (Third Quartile): The value below which 75% of the data falls. It is also the median of the upper half of the dataset.
# 
# Maximum: The largest value in the dataset.

# Question: 4
# What is correlation? Give an example with a dataset & graphical representation on jupyter Notebook
# 
# Correlation is a statistic that establish the relationship  between two variables. It indicates how closely the variables move together.
# It indicates how closely the variables move together.
# 
# The correlation coefficient, denoted by r, ranges from -1 to 1:

# In[8]:


#for example of correlation 
import numpy as np
import matplotlib.pyplot  as plt
hours_study = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_score = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
correlation_coefficient = np.corrcoef(hours_study, exam_score)[0, 1]

print("Correlation coefficient:", correlation_coefficient)

plt.scatter(hours_study, exam_score, color='red')
plt.title('Hours Study vs. Exam Score')
plt.xlabel('Hours Study')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()


# Deep learning
# Question: 1
# 
# (a) Explain how you can implement DL in a real-world application.
# 
# Implementing Deep Learning (DL) in a real-world application involves several steps and considerations. Here's a general outline of how you can implement DL in a real-world application:
# 
# Define the Problem
# Data Collection
# Data Preprocessing
# Model Selection
# Model Training
# Hyperparameter Tuning
# Model Evaluation
# Deployment
# 
# Deep learning models can learn efficiently on tabular data and allow us to build data-driven intelligent systems. The above-discussed data forms are common in the real-world application areas of deep learning.
# 
# (b) What is the use of Activation function in Artificial Neural Networks? What would be the problem if we don't use it in ANN networks.
# Activation functions are crucial components of artificial neural networks (ANNs) that introduce non-linearity into the network, enabling it to learn complex patterns and relationships in the data. 
# 
# If activation functions are not used in artificial neural networks (ANNs), several problems arise, significantly limiting the network's ability to learn and perform effectively:
# 
# Linearity: Without activation functions, the network would reduce to a series of linear transformations.
# Expressiveness: Activation functions introduce non-linearity into the network, enabling it to approximate complex functions and capture non-linear relationships in the data.
# Vanishing Gradient: The absence of activation functions can lead to the vanishing gradient problem, where gradients become increasingly small as they propagate backward through the network during training.
# Limited Learning Capacity: Activation functions play a crucial role in facilitating the learning process by enabling backpropagation, the algorithm used to update the network's parameters during training.
# 
# the absence of activation functions in ANN networks severely limits their expressive power, learning capacity, and ability to capture complex patterns and relationships in the data. 
# 

# In[ ]:




