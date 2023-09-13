

def get_primes(n):
    """the Sieve of Eratosthenes algorithm"""

    numbers = list(range(2, n+1))
    stop = n ** (1/2)

    for ix,_ in enumerate(numbers):
        current = numbers[ix]

        if current is None:
            continue
        elif current > stop:
            break
        else:
            numbers[ix::current] = [current] + [None] * (n//current - 1)
 
    return [n for n in numbers if n]



primes = get_primes(121)
print(primes)
