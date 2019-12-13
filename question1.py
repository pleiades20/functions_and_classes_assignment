#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of numbers as input and returns the index location
within the list of the largest number. If there is more than one location within the
list that contains the largest number, then have the function return the LAST index
location. For example, f([1,2,3,2,3,1]) should return 4.
"""
def f(l):
    ##########YOUR CODE HERE##########
    X = l[::-1]
    a = len(X)-1
    b = X.index(max(X))
    return a-b

y = f(l)
print(y)
    ###########END CODE###############