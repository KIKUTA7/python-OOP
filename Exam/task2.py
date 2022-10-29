""" Task 2 [5 points]"""
from functools import *
""" 
Write a function that takes a list of tuples, where each
tuple contains 2 integers (lower and upper bounds) and a
list of numbers. Function should return a list of only those
lists, that have numbers contained between lower and upper
bounds. For example: (4,7, [4,4,6,4,7]) this is a good tuple
and list [4,4,6,4,7] should remain in the answer. But, 
(2,5,[1,2,4,2]) is not a good list as 1 is not between 2 and 
5 and list [1,2,4,2] should be omiTted from the answer.

NOTE: Only lambda functions and following HOF functions can be 
used to solve this task: takewhile, dropwhile, zip, filter, map,
reduce, enumerate, sorted, any, all, 

NOTE: You will get partial scores if the above rule is violated.

Ex.: [(1,5,[2,3,4]), (2,12,[1,2,3,10]), (3, 4, [])] -> [[2,3,4],[]]
"""
def inRangeFilter(lst):
    return list(map(lambda x: x[2],
                filter(lambda x: all(
                    map(lambda y: y >= x[0] and y <= x[1], x[2])),lst
                    )
                    ))


print(inRangeFilter([(1,5,[2,3,4]), (2,12,[1,2,3,10]), (3, 4, [])]))

