# Task 1

str1 = input("1: ")
ans = ""
for c in str1:
    if(c == 'a'): ans+="#"
    else: ans+=c
print(ans)

# Task 2

str1 = input("2: ")
ans = ""
for c in str1:
    if(ord(c) >= ord('e') and ord(c) <= ord('l')): ans+=c.upper()
    else: ans+=c
print(ans)

# Task 3
dic ={
    "B": "K",
    "A": "C"
}
dic1 = {}
for k in dic.keys():
    dic1[dic.get(k)] = k
print(dic1)

# Task 4
lis = list(input("4: "))
MX = -1
for c in lis:
   if(not c == ' '): MX = max(int(c),MX)
print(MX)

# Task 5
lis = list(input("5: "))
dic = {}
MX = -1
i = -1
for l in lis:
    if(not l == ' '): dic.__setitem__(l,0)
for l in lis:
    if(not l == ' '): dic.__setitem__(l,dic.get(l) + 1)
for l in lis:
    if(not l == ' '):
        if(MX < dic.get(l)):
            MX = dic.get(l)
            i = int(l)
print(i)

# Task 6

lis = [("Beqa",4.0)]
dic = {}
for l in lis:
    dic.__setitem__(l[0],l[1])

print(dic)

# Task 7
tupoi1 = (1,2,4,5,3,7,0)
tupoi2 = (1,9,2,7,4,8,8)
tupoi3 = []
for k in tupoi1:
    if(tupoi2.__contains__(k)):
        tupoi3.append(k)
tup = tuple(tupoi3)
print(tup)





# Task 8
N = int(input("8: "))
lis = []
list1 = [1]
lis.append(list1)
list1 = [1,1]
lis.append(list1)
index = 1
for i in range(N - 2):
    list1 = []
    index+=1
    f = 0
    for k in range(index + 1):
        if(k==0):
            f = lis[index - 1][0]
            list1.append(lis[index - 1][0])
        elif (k == index): list1.append(lis[index - 1][index - 1])
        else:
            s = lis[index - 1][k]
            list1.append(f + s)
            f = lis[index - 1][k]
    lis.append(list1)
print(lis)












