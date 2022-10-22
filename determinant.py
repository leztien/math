"""recursive determinant"""


import random
import numpy as np



def make_matrix(n):
    return [[random.randint(-10,10) if random.randint(0,1) else 0
             for j in range(n)] for i in range(n)]


def select_row(A):
    counts = [sum(bool(a) for a in row) for row in A]
    mn = min(counts)
    for i in range(len(A)):
        if counts[i] == mn:
            return i


def submatrix(A,i,j):
    n = len(A)
    return [[A[i_][j_] for j_ in range(n) if j_ != j] for i_ in range(n) if i_ != i]


def det(A):
    n = len(A)
    # base case
    if n == 2:
        (a,b),(c,d) = A[0], A[1]
        return a*d - c*b
    # recursive case
    i = select_row(A)
    Summe = 0 # sum
    for j in range(n):
        if A[i][j] == 0:
            continue
        Summe += (-1)**(i+j) * A[i][j] * det(submatrix(A,i,j))
    return Summe

##############################################################



n = random.randint(2,10)
A = make_matrix(n)

print(*A, sep='\n')

d = np.linalg.det(A)
print(d)

d = det(A)
print(d)
