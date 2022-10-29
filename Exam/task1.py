""" Task 1 [4 points]"""

"""
This assignment is a quizz. You should answer
4 questions are given below. Each question has
exactly one correct answer and is worth 1 point.

You should mark your choice with 'x'.

Example:
~~~
Question?
[ ] Not selected
[X] Selected

NOTE: If you mark more than one answer, delete or
modify part of the question, you will get 0 for that
question.
"""

# Question 1

"""
Which of the following are false in Python?

A. All elements in the list should have same type.
B. Elements in the list can be modified.
C. List has dynamic size.

[X] Only A
[ ] A and B
[ ] only C
[ ] A and C
"""

# Question 2

"""
Which structure is immutable in python?

[ ] List and String
[ ] Dictionary and Tuple
[ ] List and Tuple
[X] String and Tuple
"""

# Question 3

def fun3(N, M, K):
    lst = []
    for i in range(M-5):
        lst.append(i)
    for j in range(M+2):
        for i in range(K):
            lst.append(j+i)
    return lst

"""
What is the time complexity of the given function?

[X] O(M*K)
[ ] O(N*M)
[ ] O(N+M*K)
[ ] O(M+K)
"""

# Question 4

def fun4(n):
    if n == 1:
        return 1
    else:
        return n + fun4(n-1)

"""
What is the time complexity of the given function?

[ ] O(1)
[ ] O(logN)
[X] O(N)
[ ] O(N*N)
"""