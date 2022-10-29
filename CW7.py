# Task 1

def BitCount ( k ):
    count = 0
    bi = str(bin(k))
    while (bi ):
        if(bi[0] == '1') :
         count += 1
        bi = bi[1:]

    return count

print(BitCount(7))

# Task 2

def CountBitsOn (*nums) :
    bi = nums[0]
    for k in range(1,len(nums)):
        bi = bi & nums[k]
    return BitCount(bi)

print(CountBitsOn(5,7))

# Task 3

def flip (k):
    str1 = bin(k)
    str2 = "0b"
    for j in range(2,len(str1)):
        if(str1[j] == '0'):
            str2 = str2 +  '1'
        else : str2 = str2 + '0'

    return int(str2,2)


print(flip(8))

# Task 4

def toBitList (k):
    str1 = bin(k)
    ans = []
    for j in range(2,len(str1)):
        ans.append(str1[j])
    return ans

print(toBitList(10))

# Task 5

def setFirstOn (k):
   str1 = bin(k)
   str2 = ""
   for j in range(len(str1) - 1):
       str2 += str1[j]
   str2+='1'

   return int(str2 , 2)

print(setFirstOn(4))

# Task 6
                  #   mokle versia
# def tripleCount(N):
#     count = 0
#     for i in range(N):
#         if bin(i).count("1") == 3:
#             count += 1
#     return count
                   #  mokle versia(end)


def trippleCount (k):
    ans = 0
    for i in range(k):
        str1 = bin(i)
        count = 0
        for j in range(len(str1)):
            if(str1[j] == '1'):
                count +=1
        if(count == 3):
            ans+=1
    return ans

print(trippleCount(31))

# Task 7

def listXor (list , k):
    # modlst = [x ^ K for x in lst]
    # return modlst
    newlis = []
    for j in list:
        newlis.append(j ^ k)
    return newlis

print(listXor([1,4,7,2,3],5))

# Task 8

def filterOdd (list):
    newlis = []
    for k in range(len(list)):
        if (not bin(list[k])[len(bin(list[k])) - 1] == "1"):
            newlis.append(list[k])
    return newlis

print(filterOdd([1,2,3,4]))

# Task 9

def f (k):
    return k == 1 or k == 3

def filter (list , func):
    ans = []
    for k in range(len(list)):
        if(func(list[k])):
            ans.append(list[k])

    return ans

print(filter([1,2,3,4],f))

# Task 10

def bit3RangeList (L,R):
    ans = 0
    for k in range(L,R + 1):
       if(k % 8 >= 4):
          ans +=1

    return ans

print(bit3RangeList(5,9))

# Task 11

def filterEven (list):
    newlis = []
    for k in range(len(list)):
        if (bin(list[k])[len(bin(list[k])) - 1] == "1"):
            newlis.append(list[k])
    return newlis

def multipleOddRangeList (list):
    ans = []
    for (a,b) in list:
        temp = []
        for k in range(a,b + 1):
            temp.append(k)
        ans.append(filterEven(temp))

    return ans

print(multipleOddRangeList([(1,5),(2,5),(17,12),(10,14)]))




