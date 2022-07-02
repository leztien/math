

"""
Get all divisors of a number. 
Alle Teiler einer Zahl ermitteln.

'get_all_divisors' is the main function, the others are helper-functions.
"""


from operator import mul
from functools import reduce



def combinations(seq, r):
    """same functionality as itertools.combinations, 
    however probably a more elegant implementation is possible"""
    
    combinations = []
    
    def recurse(s, r, depth = 0):
        if depth == r:
            combinations.append([])
            return

        mx = (-r+1) + depth if (-r+1) + depth !=0 else len(s)
        
        for i,e in enumerate( s[0: mx] ):
            recurse(s[1+i:], r, depth+1)
            
            for combination in combinations:
                if len(combination) == r - depth - 1:
                    combination.append(e)
    recurse(seq, r)
    return tuple(tuple(e)[::-1] for e in combinations)


def powerset(s):
    return [set(e) for r in range(len(s)+1)
                   for e in combinations(s, r)]


def multipowerset(s):
    return [tuple(e) for r in range(len(s)+1)
                   for e in combinations(s, r)]


def unique_multipowerset(s):
    return set(e for e in multipowerset(s) if e)


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


def get_all_divisors(number):
    factors = primfactorzerlegung(number)
    combinations = unique_multipowerset(factors)
    return [1,] + sorted(reduce(mul, seq) for seq in combinations)



#Test
if __name__ == "__main__":
    from random import randint
    
    MAX = 500
    
    for test in range(MAX*2):
        number = randint(1, MAX)
        divisors = get_all_divisors(number)
        
        print(f"\nnumber = {number}, divisors = {divisors}")
        
        #test 1
        for divisor in divisors:
            if number % divisor:
                raise Exception("error 1")
        #test 2
        for n in set(range(2, number)) - set(divisors):
            if not(number % n):
               raise Exception("error 2") 
    else:
        print("\nAll tests passed.")


