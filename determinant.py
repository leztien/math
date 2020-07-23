"""recursive function that calculates the determinant of a matrix"""

import numpy as np
n = np.random.randint(2,10)
A = np.random.randint(-10,10, size=(n,n))



from itertools import cycle
def determinant(A):
    #base case
    if A.shape == (2,2):
        a,b,c,d = A.ravel()
        return a*d-b*c  # 2x2 matrix determinant
    #recursive case
    return sum(scalar * sign * determinant(np.delete(A[1:], j, axis=1)) 
               for j,(scalar,sign), in enumerate(zip(A[0], cycle([+1, -1]))))
        
    

ans = determinant(A)
print(ans)


#compare with numpy
from numpy.linalg import det
d = det(A)
print(d)
