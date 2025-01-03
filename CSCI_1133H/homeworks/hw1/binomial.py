# Rohit Poduval, poduv006
# binomial.py
# HW1


import math


def choose(n, k):
    if not (0 <= k <= n):
        raise Exception("The formula only works when 0 <= k <= n")
    else:
        return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))


def main():
    print(choose(5, 2))  # prints 1326


if __name__ == "__main__":
    main()
