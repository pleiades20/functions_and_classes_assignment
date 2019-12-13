#########IMPORT LIBRARIES HERE IF NEEDED#######
import datetime
################END IMPORTS####################
"""
Write a function that takes 2 strings s1 and s2 as inputs. These strings will represent times of the day and will be written in the format
HH:MM:SS. Your function should return the number of seconds between these 2 times. You may assume s2 always represents a later time than s1.
There are a number of ways to do this problem, but you will find making use of the datetime.datetime and datetime.timedelta modules will make
things easiest. For example, f('08:59:59','10:24:31') should return 5072.
"""
def f(s1, s2):
    ##########YOUR CODE HERE##########
    time1 = datetime.datetime.strptime(s1, '%H:%M:%S')
    time2 = datetime.datetime.strptime(s2, '%H:%M:%S')
    S = time2 - time1
    return S.seconds

y = f(s1, s2)
print(y)
    ###########END CODE###############
