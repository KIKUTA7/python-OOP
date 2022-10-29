# Task 1

def fileLen (inp):
    file = open(inp , "r")
    str = file.readline()
    ans = 0
    while (not  str == ""):
        ans += len(str)
        str = file.readline()
        if(len(str) > 0  ): ans -=1

    file.close()
    return ans

file = "C:\\Users\\beqak\\OneDrive\\Desktop\\file.txt"
print(fileLen(file))
# Task 2

def fileToList (inp):
    file = open(inp , "r")
    str = file.readline()
    ans = []
    while (not  str == ""):
        ans.append(str)
        str = file.readline()

    file.close()
    return ans

print(fileToList(file))
# Task 3

def lowerCaseCount (inp):
    file = open(inp , "r")
    str = file.readline()
    ans = 0
    while (not  str == ""):
        for k in str:
            if (ord('a') <= ord(k) and ord(k) <= ord('z')):
                ans+=1
        str = file.readline()

    file.close()
    return ans

print(lowerCaseCount(file))
# Task 4

def copyData (inp , fi2):
    file = open(inp , "r")
    str = file.readline()
    file2 = open(fi2 , "a")
    while (not  str == ""):
        file2.write(str)
        str = file.readline()

    file.close()

file2 = "C:\\Users\\beqak\\OneDrive\\Desktop\\file2.txt"
copyData(file , file2)
# Task 5

def fileStats (inp):
    file = open(inp , "r")
    str = file.readline()
    ans = {}
    while (not  str == ""):
        for k in str :
            if(not ans.get(k) == None):
                ans[k]+=1
            else : ans[k] = 1
        str = file.readline()

    file.close()
    return ans

print(fileStats(file))

# Task 6

def countFrequency (inp , str1):
    file = open(inp , "r")
    str = file.readline()
    ans = 0
    while (not  str == ""):
        ans += str.count(str1)
        str = file.readline()

    file.close()
    return ans

print(countFrequency(file , "ab"))
# Task 7

def rec_C (n, k):
    if(n == k): return 1
    if(k == 1): return 1
    if(n == 1): return 1
    return rec_C(n - 1 , k - 1) + rec_C(n - 1 , k)

print(rec_C(5,4))
# Task 8

def rec_reverse (str1):
    if(len(str1) == 1): return str1
    else:
        ans = rec_reverse(str1[1:])
        ans += str1[0]
        return ans

print(rec_reverse("abcd"))
# Task 9

def rec_merge (lis1 , lis2):
    anslis = []

    if lis1[0] < lis2[0]:
        anslis.append(lis1[0])
        if(len(lis1) > 1):
         for k in rec_merge(lis1[1:],lis2):
             anslis.append(k)
        else:
             for k in lis2:
                 anslis.append(k)
    else:
        anslis.append(lis2[0])
        if(len(lis2) > 1):
            for k in rec_merge(lis1, lis2[1:]):
                anslis.append(k)
        else:
            for k in lis1:
                anslis.append(k)
    return anslis

print(rec_merge([1,3,5,7],[2,4,6,8]))
# Task 10

def merge_sort (lis):
    if(len(lis) == 1): return lis
    k = len(lis) // 2
    half1 = merge_sort(lis[0:k])
    half2 = merge_sort(lis[k:])
    return rec_merge(half1 , half2)

print(merge_sort([1,5,2,54,3,6]))
# Task 11

def guess_num (L , R  ):
    if (L == R): return L
    else:
        mid = ( L + R ) // 2
        str1 = "Is " + str(mid) + " greater than your number?"
        str2 = input(str1)
        if(str2 == "y"):
            return guess_num(L , mid - 1 )
        else:
            str2 = input("Is " + str(mid) + " your number?")
            if(str2 == "y"): return mid
            else:
             return guess_num(mid + 1 , R )


print(guess_num(int(input("LOW: ")),int(input("HIGH: "))))













