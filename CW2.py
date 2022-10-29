# Task 1
x = int(input("> "))

if(abs(x) <= 10 and x % 2 == 1):
    print("First category")
elif (abs(x) <= 100 and (x % 10 == 2 or x % 10 ==3)):
    print("Second category")
else:
    print("Third category")

# Task 2
n = int(input("> "))
arr = []
for i in range(1,n+1):
    if n % i == 0: arr.append(i)
    str1 =""
for i in arr:
    str1 +=" "+ str(i)
print("Divisors of "+ str(n) + " are:" + str1)

# Task 3
# A

i = 0
while i < 26 :
    print(chr(ord('a')+i),end=" ")
    i+=1
print("")
#B
for i in range(26):
    print(chr(ord('a')+i),end=" ")
    i+=1
print("")
# Task 4
p = int(input("> "))
k = 0
for i in range(1,p+1):
        if(p % i == 0):
            k+=1
if(k == 2): print("YES")
else: print("NO")

# Task 5

n = int(input("> "))
arr = []
arr.append(0)
for i in range(1,n+1):
    arr.append(0)

for k in range(2,n):
    if(arr[k] == 0):
        print(k , end=" ")
        j = k
        while j <= n:
            arr[j] = 1
            j+=k

# Task 6

n = int(input("> "))

f = 0
s = 1

for i in range(1,n+1):
    if(i == 1): print (f, end=", ")
    elif(i == 2): print(s, end=", ")
    else:
        if(i == n):
            print(f + s, end="")
        else:
            print(f + s, end=", ")
        k = f
        f = s
        s = k + s

# Task 7

for a in range(101):
    for b in range(101):
        for c in range(101):
            if(a*b - c ** 2 == 0):
                print(a,b,c)

# Task 8
n = int(input("> "))
for i in range(1,n+1):
    print((n-i)*'.' + str(i) * i)


# Task 9
n = int(input("> "))
k = 0
for i in range(n):
    for j in range(n):
        if(k == 0):
            print("#",end="")
        else :
            print("*", end="")
        k+=1
        k=k%2
    print("")






