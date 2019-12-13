#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of numbers as input and returns the median of the list.
"""
def f(l):
    ##########YOUR CODE HERE##########
    N = len(l)
    l.sort()
    if N % 2 == 0:
        median_a = N/2
        median_b = N/2 + 1
        median1 = int(median_a) - 1
        median2 = int(median_b) - 1
        return (l[median1] + l[median2]) / 2
    else:
        median_a = (N + 1) / 2
        median1 = int(median_a) - 1
        return l[median1]

y = f(l)
print(y)
    ###########END CODE###############
