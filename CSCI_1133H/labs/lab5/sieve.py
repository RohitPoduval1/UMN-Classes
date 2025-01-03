# Lab 5
# sieve.py


def sieve(n):
    potential_primes = [i for i in range(2, n+1)]  # populate the list with numbers 2 to n
    primes = potential_primes[:]

    for i in range(len(potential_primes)):
        for potential_prime in primes:
            if potential_prime % potential_primes[i] == 0 and potential_prime != potential_primes[i]:  # if the number is divisible by another 
                if potential_prime in primes:                                                          # and it's not the same number (because all numbers are divisible by themselves)
                    primes.remove(potential_prime)  # remove it from the list of primes because it is not prime

    return primes


print(sieve(13))
