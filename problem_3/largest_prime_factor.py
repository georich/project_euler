from math import sqrt

target = 600851475143
primes = []

for i in range(3, int(sqrt(target)), 2):
    if target % i == 0: # is a factor
        prime = 1
        for x in range(i - 2, 1, -2):
            if i % x == 0: # not a prime
                prime = 0
        if prime:
            primes.append(i)

print(f"The largest prime factor of {target} is {primes[-1]}")
