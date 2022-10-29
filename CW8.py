from itertools import *
from functools import *

# Task 1

def MultipleofK (lis,k):
    return list(filter(lambda x: x%k == 0,lis))


# Task 2

def SumOfOdds (lis):
    return reduce(lambda x, y: x + y,list(filter(lambda x: x % 2 != 0 , lis )),0)

# Task 3

def removeEverySecond (lis):
    # newLis = list(enumerate(lis))
    # return [x[1] for x in list(filter(lambda x: x[0] % 2 == 0, newLis))]


    return [y[1] for y in list(filter(lambda x: x[0] % 2 == 0,list(enumerate(lis))))]



# Task 4
def DictWithDivisors (lis):
    return dict(zip(lis , list(map(lambda x: [y for y in range(1,x+1) if (x % y == 0)],lis))))

print(DictWithDivisors([1,2,3,4]))
# Task 5

def Map (func , lis):
    return [func(x) for x in lis]

def Filter (func , lis):
    return [x for x in lis if(func(x))]

def takeWhile (func , lis):
     ans = []
     iterator = 0
     while (func(lis[iterator])):
             ans.append(lis[iterator])
             iterator +=1

     return ans

def dropWhile (func , lis):
    ans = []
    iterator = 0
    for iteartor in range(len(lis)):
        if(func(lis[iterator])):
            return lis[iterator:]

def Enumerate (lis):
    ans = []
    for iterator in range(len(lis)):
        ans.append((iterator,lis[iterator]))
    return ans

def Zip (*lists):
    ans = []
    lenmin = len(lists[0])
    for listsmember in lists:
        if(lenmin >= len(listsmember)):
            lenmin = len(listsmember)

    for iterator in range(lenmin):
      helplis = []
      for k in lists:
          helplis.append(k[iterator])
      ans.append(tuple(helplis))
    return ans

def Reduce (func , lis , base):
    ans = base
    for iterator in lis:
        ans = func(iterator,ans)

    return ans








