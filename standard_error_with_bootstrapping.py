"""Estimating SE with bootstrapping"""

import random
from math import sqrt


def std(sample, df=1):
    mu = sum(sample) / len(sample)
    return (sum((x - mu)**2 for x in sample) / (len(sample) - df)) ** 0.5


U = lambda : random.uniform(0, random.randint(1, 10))
N = lambda : random.gauss(random.randint(-100, 100), random.randint(0, 5))
D = U if random.randint(0,1) else N

#########################################################

m = 10000
population = [D() for _ in range(m)]

n = 10
sample = random.sample(population, k=n)

s = std(sample)
SE = s / sqrt(n)
print("formula SE   =", round(SE,3))

statistics = []
for _ in range(100):
    resample = random.choices(sample, k=len(sample))
    mean = sum(resample) / len(resample)
    statistics.append(mean)

SE = std(statistics, df=0)
print("bootstrap SE =", round(SE,3))
