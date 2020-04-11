def is_prime(number):
    if number == 1:
        return False
    
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    else:
        return True
    
    
def generate_primes(start=1):
    number = start
    while True:
        if is_prime(number):
            yield number
        number += 1


class Primes:
    def __init__(self):
        self.list = []
        self.g = generate_primes()
    
    def __getitem__(self, ix):
        while ix > len(self.list)-1:
            self.list.append(next(self.g))
        return self.list[ix]
    
    def __str__(self):
        return str(self.list)
    def __repr__(self):
        return self.__str__()


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
        else:
            ix += 1
    #check
    from operator import mul; from functools import reduce
    assert reduce(mul, factors) == number, "wrong result"
    
    #turn into a string
    exponents = [chr(n) for n in (0x2070, 0x00b9)] + [chr(n) for n in (0x00b2, 0x00b3) + tuple(0x2074+i for i in range(0,6))]
    exponents += [str.join('',(exponents[int(d)] for d in str(n))) for n in range(10, 999)]
    
    #loop
    string = []
    counter = 0
    factors += [None,]  # for technical reasons

    for i in range(len(factors)):
        counter += 1
        
        if i==0 or (factors[i] != factors[i-1]):
            if counter >= 2:
                string.append(str(exponents[counter]))
            
            if not factors[i]: break
            string.append(" × " + str(factors[i]))
            counter = 0
    string = str.join('', string)[3:]
    return string


############################

number = 2**200 * 3**5 * 7**231
ans = factorize(number)
print(ans)
