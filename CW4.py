def max3 (a,b,c):
    return max(max(a,b),c)
def alphaCounter ( str1 , c) :
    return str1.count(c)

def listSum (ls):
    result = 0
    for k in ls:
        result += k
    return result

def removeAll (ls, ls2):
    ansls = []
    for k in ls:
        t = False
        for j in ls2:
            if(j == k):
                t = True
                break
        if(not t): ansls.append(k)
    return ansls

def extendWith (str1 , tup):
     ls = list(tup)
     return str1 + ls[0] * ls[1]

def tupleIntersection (tup1 , tup2 , tup3):
    ls1 = list(tup1)
    ls2 = list(tup2)
    ls3 = list(tup3)
    ls4 = [value for value in ls1 if value in ls2]
    ls4 = [value for value in ls4 if value in ls3]
    return tuple(ls4)

# for k in tup1:
#   for e in tup2 and e in tup3: aq shedareba mere e == k , amis dawera mosula

def avrg (nums):
    sum = 0
    k = 0
    for i in nums:
        sum +=i
        k+=1
    return sum / k

def printCarData (**kwargs) :
    if(kwargs.get("Manufacturer") == None) :
        print("Unknown")
    else: print(kwargs["Manufacturer"])
    if (kwargs.get("Model") == None):
            print("Unknown")
    else: print(kwargs["Model"])
    if (kwargs.get("Category") == None):
            print("Unknown")
    else: print(kwargs["Category"])
    if (kwargs.get("Price") == None):
         return "Unknown"
    else : return kwargs["Price"]

# debilo : kwargs.get("Price" , "Unknown") da egaa default value aris Unknown


def concatinate (*strs):
    ans = ""
    for c in strs:
        ans +=c
    return ans

