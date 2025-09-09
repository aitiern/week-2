import numpy as np


# update/add code below ...
# Exercise 1
def ways(n):
    combos = []
    # loop over possible numbers of nickels
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        combos.append((pennies, nickels))
    return len(combos), combos

# Test cases
print(ways(12))  # (3, [(12, 0), (7, 1), (2, 2)])
print(ways(20))  # (5, [(20, 0), (15, 1), (10, 2), (5, 3), (0, 4)])
print(ways(3))   # (1, [(3, 0)])
print(ways(0))   # (1, [(0, 0)])



# Exercise 2

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
names_scores = np.concatenate((names, scores))

# Part 1
# Use NumPy to write a function lowest_score(names, scores) that returns the name of the student with the lowest score.

def lowest_score(names, scores):
    score_index = np.argmin(scores)               # index of the lowest score
    low_student = names[score_index]              # corresponding student
    low_score = scores[score_index]               # corresponding score
    return low_student, low_score

print(lowest_score(names, scores))

# Part 2
'''
Write a similar function sort_names(names, scores) that will list the names of students in descending order of test score
(i.e., a list of names, with associated scores in order from highest to lowest).
'''

def sort_names(names, scores):
    # argsort sorts ascending by default, so we flip with [::-1]
    sorted_indices = np.argsort(scores)[::-1]
    sorted_names = names[sorted_indices]
    sorted_scores = scores[sorted_indices]
    
    # Return as list of (name, score) tuples
    return list(zip(sorted_names, sorted_scores))

print(sort_names(names, scores))
