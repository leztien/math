

"""
Primfaktorenzerlegung für den ggT und kgV
Seite 9, 11 Grundwissen Mathematik
"""


from collections import Counter
from functools import reduce
from operator import mul



def ggT(a, b):
    while b:
        a, b = b, a % b
    return a


def kgV(a, b):
    return abs(a * b) // gcd(a, b)


def is_prime(n):
    if n == 2 or n == 5:
        return True
    if n <= 1 or n % 2 == 0 or str(n).endswith('5'):
        return False

    for i in range(3, n, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True 

    
def primes_generator():
    k = 1
    while True:
        k += 1
        if is_prime(k):
            yield k
        

def primfactorzerlegung(n):
    factors = []
    g = primes_generator()
    f = next(g)
    while n > 1:
        if n % f == 0:
            n = n // f
            factors.append(f)
        else:
            f = next(g)
    
    g.close()
    return factors


# test function
def kanonische_primfaktorenzerlegung(n):
    if n <= 1: return None
    factors = []
    def recursive(n):
        # Base Case
        if is_prime(n):
            factors.append(n)
            return
        
        # Recursive Case
        f = int(n ** (1/2))
        while True:
            if n % f == 0:
                break
            else:
                f -= 1
                continue
        # recurse from here
        recursive(f)
        recursive(n // f)
    # Start recursion
    recursive(n)
    return sorted(factors)



def multiset_conjunction(list1, list2):
    c = Counter()
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    keys = set(c1.keys()).intersection(c2.keys())
    
    for k in keys:
        c[k] = min(c1[k], c2[k])

    return sum([[k]*c[k] for k in sorted(c.keys())], [])
    
    
    
def multiset_disjunction(list1, list2):
    c = Counter()
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    keys = set(c1.keys()).union(c2.keys())
    
    for k in keys:
        c[k] = max(c1[k], c2[k])

    return sum([[k]*c[k] for k in sorted(c.keys())], [])


def gcd(a,b):
    list1 = primfactorzerlegung(a)
    list2 = primfactorzerlegung(b)
    common = multiset_conjunction(list1, list2)
    return reduce(mul, common) if common else 1


def lcm(a,b):
    list1 = primfactorzerlegung(a)
    list2 = primfactorzerlegung(b)
    common = multiset_disjunction(list1, list2)
    return reduce(mul, common)
    






# Test
if __name__ == "__main__":
    from random import randint
    
    print("\nTest 1:")
    for _ in range(100):
        n = randint(2, 150)
        zerlegung1 = primfactorzerlegung(n)
        zerlegung2 = kanonische_primfaktorenzerlegung(n)
        print(n, zerlegung1, zerlegung2, zerlegung1 == zerlegung2)
        if zerlegung1 != zerlegung2:
            raise Exception("error")
    
    print("\nTest 2:")
    for _ in range(100):
        mx = randint(3, 500)
        a,b = (randint(2, mx) for _ in "..")
        print("a =", a, "b =", b)
        
        gcd1 = ggT(a,b)
        gcd2 = gcd(a,b)
        
        lcm1 = kgV(a,b)
        lcm2 = lcm(a,b)
        
        assert gcd1 == gcd2 and lcm1 == lcm2, "error"
        print("gcd =", gcd1, "lcm =", lcm1)
        
        if a*b != gcd1 * lcm1:
            Exception("error")
        print("a * b =", a*b, "gcd * lcm =", gcd1 * lcm1); print()
        
    print("All tests passed")    
