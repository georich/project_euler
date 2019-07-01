from math import sqrt

def is_prime(factor):
    """Check if a given number is a prime number"""
    for x in range(factor - 2, 1, -2):
        if factor % x == 0: # not a prime
            return False
    return True

def largest_prime_factor(target):
    """Find the largest prime factor of the number given"""
    primes = []
    for i in range(3, int(sqrt(target)), 2):
        if target % i == 0: # is a factor
            if is_prime(i):
                primes.append(i)
    return primes[-1]

number = 600851475143
print(f"The largest prime factor of {number} is {largest_prime_factor(number)}")
