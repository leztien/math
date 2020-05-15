import random
import numpy as np
import matplotlib.pyplot as plt


def make_bin_breaks(probabilities):
    assert sum(probabilities)==1.0,"error"
    return [sum(probabilities[:i]) for i in range(1,len(probabilities)+1)]
    

def discretize(value, bins):
    for bin_number, bin_break in enumerate(bins):
        if value < bin_break:
            return bin_number
    else:
        return bin_number+1


def generate_from_discreet_distribution(probabilities, n=1000):
    bins = make_bin_breaks(probabilities)
    return [discretize(random.random(), bins=bins) for _ in range(n)]
    
#----------------------------------------------------------------------
    

def f1(x,y):
    return np.matmul([(0, 0),(0, 0.16)], [x,y])

def f2(x,y):
    return np.matmul([(0.85, 0.04),(-0.04, 0.85)], [x,y]) + [0, 1.6]

def f3(x,y):
    return np.matmul([(0.2, -0.26),(0.23, 0.22)], [x,y]) + [0, 1.6]

def f4(x,y):
    return np.matmul([(-0.15, 0.28),(0.26, 0.24)], [x,y]) + [0, 0.44]

ff = (f1, f2, f3, f4)


###########################################################


p = (0.01, 0.85, 0.07, 0.07)  #must sum to 1.0
m = 50000
arr = generate_from_discreet_distribution(probabilities=p, n=m)

point = (0,0)
points = [point,]

for ix in arr:
    point = ff[ix](*point)
    points.append(point)
    
    
mx = np.vstack(points)

plt.figure(figsize=(10,10))
plt.plot(*mx.T, 'k.', markersize=2)
plt.axis("equal")
