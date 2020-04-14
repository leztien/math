def is_prime(number):
    if number == 1: return False
    for divisor in range(2, number):
        if number % divisor == 0: return False
    return True
    
    
def generate_primes(start=1):
    number = start
    while True:
        if is_prime(number): yield number
        number += 1


class Primes:
    def __init__(self):
        self.list = []
        self.g = generate_primes()
    def __getitem__(self, ix):
        while ix > len(self.list)-1: self.list.append(next(self.g))
        return self.list[ix]
    def __str__(self): return str(self.list)
    def __repr__(self): return self.__str__()


primes = Primes()

def factorize(number):  # Primfaktorzerlegung
    global primes
    quotient = number
    factors = []
    ix = 0
    while quotient > 1:
        if quotient % primes[ix] == 0:
            factors.append(primes[ix])
            quotient //= primes[ix]
        else: ix += 1
    return tuple(factors)



from collections import Counter
from operator import mul, and_, or_
from functools import reduce

def GCD(*numbers):
    multisets = (Counter(factorize(n)) for n in numbers)
    factors = tuple(reduce(and_, multisets).elements())
    return reduce(mul, factors) if factors else 1

def LCM(*numbers):
    multisets = (Counter(factorize(n)) for n in numbers)
    factors = tuple(reduce(or_, multisets).elements())
    return reduce(mul, factors if factors else numbers)

def check_gcd_lcm(number1, number2, gcd, lcm):
    return number1 * number2 == gcd * lcm


#####################################################################################

n1,n2 = 180, 585

ans = factorize(n1)
print(ans)

ans = factorize(n2)
print(ans)

#----------------------

gcd = GCD(n1, n2)
print("GCD =", gcd)

#----------------------

lcm = LCM(n1, n2)
print("LCM =", lcm)

#----------------------

b = check_gcd_lcm(n1, n2, gcd, lcm)
print("correct =", b)

#...........................................

gcd = GCD(180, 585, 3003)
print("GCD =", gcd)

lcm = LCM(180, 585, 3003)
print("LCM =", lcm)
