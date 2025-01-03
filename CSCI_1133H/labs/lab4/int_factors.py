# Lab 4
import math


# int -> boolean
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:  # if the number is divisible by numbers less than it...
            return False  # it is not prime
    return True

    
# takes in an integer and produces a list of the factors ordered from least to greatest
# int -> list
def factorize(num):
    NUMBER = num  # the number to be factored (a constant)
    factors = []  # the numbers that are part of the prime factorization (does not include repeats)
    prime_factorization = [] # the complete factorization including repeats

    if is_prime(num):
        prime_factorization.append(num)
        return prime_factorization
    
    else:
        for i in range(2, round(math.sqrt(num) + 1)):
            if is_prime(i):
                if num % i == 0:
                    factors.append(i)

        for factor in factors:

            # see how many of the factors can fit into the number
            # then see how many of the next factors can fit into that remainder
            while (num / factor).is_integer():
                num /= factor
                prime_factorization.append(factor)
                    
        return prime_factorization        


def get_positive_integer():
    num = int(input("Input a positive integer: "))
    while not(num > 0 and (isinstance(num, int) or num.is_integer())):
        print("Input an integer greater than zero")
        num = int(input("Input a positive integer: "))
    return num
    
def main():

    num = get_positive_integer()
    print("Factors: ", end="")
    print(*factorize(num), sep="*", end="")
    print()

    keep_going = input("Continue (y/n)?: ")
    while keep_going.lower() == "y":
        num = get_positive_integer()
        if num > 0 and (isinstance(num, int) or num.is_integer()):
            print("Factors: ", end="")
            print(*factorize(num), sep="*", end="")
            print()
        keep_going = input("Continue (y/n)?: ")
    
    
if __name__ == "__main__":
    main()
