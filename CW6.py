# Task 1

def numstairs (n):
    if(n == 2): return 2
    if(n == 1): return 1
    if(n == 0): return 0
    if(n < 0): return 0
    return numstairs(n - 2) + numstairs(n - 1)

print(numstairs(5))
# Task 2
def classroom (file):
    f = open(file , "a")
    str = input("Input Data: ")
    while (str.lower() != "save"):
        str2 = str.split(" ")
        if(len(str2) == 6):
            if(str2[0].isalpha() and str2[1].isalpha() and
            str2[2] in ["A","B","C"] and (int(str2[3]) in range(1,11)) and
            (int(str2[4]) in range(1,11)) and (int(str2[4]) in range(1,11))):
                j = 0
                str3 = ""
                for k in str2:
                    if(j == 5):
                        str3 = str3 + k
                    else: str3 = str3 + k + "/"
                    j+=1
                f.write(str3 + "\n")
                str = input("Input Data: ")
            else:
             str = input("Incorrect Input: ")

        else:
          str = input("Incorrect Input: ")

    f = open(file, "r")
    lis = f.readlines()
    for k in lis:
        print(k , end="")



# Task 3

def findAverageOfName(firstName , lastName ):
    file = "new.txt"
    classroom(file)
    f = open(file , "r")
    for line in f.readlines():
        Firstname  = ""
        Lastname = ""
        Class = ""
        gradeEnglish = ""
        gradeMath = ""
        gradePhysics = ""
        temp = ""
        line = line + "/"
        for char in line:
            if(not char == "/"):
                temp = temp + char
            else:
                if(Firstname == ""):
                    Firstname = temp
                elif (Lastname == ""):
                    Lastname = temp
                elif (Class == ""):
                    Class = temp
                elif (gradeEnglish == ""):
                    gradeEnglish = temp
                elif (gradeMath == ""):
                    gradeMath = temp
                else:
                    gradePhysics = temp
                temp = ""
        if (firstName == Firstname and lastName == Lastname):
            return (int(gradePhysics) + int(gradeMath) + int(gradeEnglish)) / 3

print(findAverageOfName('P','P'))

# Task 4

def mySum (list):
    if(len(list) == 1): return list[0]
    return list[0] + mySum(list[1:])

# Task 5

def myPow (number , power):
    if (power < 0): return 1/(myPow(number, (-power)))
    if(power == 0): return 1
    if(power == 1): return number
    return number * myPow(number , power - 1)

# Task 6

def myGCD (integer1 , integer2):
    if(integer1 == 0): return integer2
    if(integer2 == 0): return integer1

    if(integer1 > integer2):
        return myGCD(integer1 % integer2, integer2)
    else:
        return myGCD(integer1, integer2 % integer1)


# Task 7

def mutualRecursion (input):
    def F(n):
        if(n == 0): return 1
        return n - M(F(n - 1))

    def M(n):
        if(n == 0): return 0
        return n - F(M(n - 1))

    if(input[0] == "f"):
        return F(int(input[2:len(input) - 1]))

    else:
        return M(int(input[2:len(input) - 1]))

print(mutualRecursion("m(10)"))

# Task 8

def recursiveVersionOfTurtles (startinNum , reach , target):
    if(startinNum >= target):
        return 0
    return 1 + recursiveVersionOfTurtles(startinNum*(reach + 1) , reach , target)

# Task 9

def fileEditing (file):
    newFile = "newFile.txt"
    newF = open(newFile,"a")
    f = open(file , "r")

    for line in f.readlines():
        for char in line:
            if(char == "J"):
                newF.write("I")
            else:
                newF.write(char)
        newF.write("\n")

fileEditing("new.txt")


















