

"""
Variance of a Binomial distribution
"""

from random import randint, random
k = None



def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)

def choose(n,k):
    """binomial coefficient"""
    return f(n) // (f(n-k) * f(k))

def P(X=k, n=..., p=...):
    """pmf for Binomial distribution"""
    k = X
    return choose(n,k) * p**k * (1-p)**(n-k)

def VarBinomial(n,p):
    return n * p * (1-p)

def E(X):
    return sum(x * p for x,p in X.items())

def Var(X):
    """general formula for Variance of a discrete random variable"""
    mu = E(X)
    return sum((x - mu)**2 * p for x,p in X.items())


def E_of_squared(X):
    return sum(x**2 * p for x,p in X.items())

def Var2(X):
    return E_of_squared(X) - E(X)**2




###########################################################

n = randint(2, 10)
p = random()
print(f"p = {p:.2f}, n = {n}")

X = {k:P(k, n, p) for k in range(n+1)}

var_true = VarBinomial(n, p)
var_test = Var(X)
print("binomial distribution variance = {:.2f}\ndiscrete random variable variance = {:.2f}"
      .format(var_true, var_test))
# must be equal!


var_test2 = Var2(X)
print(var_test2)



