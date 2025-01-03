# Lab 4
import math




# starts at 0
# i.e. 1 is the 0th term, 1/9 is the 1st, etc.
# returns the sum of the terms in the series provided by the lab assignment
# up to and including the nth term
def calculate_parenthesis(n_term):
    parenthesis = 0
    num = 1
    for i in range(0, n_term + 1):
        parenthesis += (((-1) ** i) / ((3 ** i) * (num)))
        num += 2
    return parenthesis


def main():
    tolerance = float(input("Enter a tolerance: "))
    
    APPROX_PI = 6 / math.sqrt(3)

    terms = 1
    while abs((APPROX_PI * calculate_parenthesis(terms-1)) - (APPROX_PI * calculate_parenthesis(terms))) >= tolerance:
        terms += 1

    print(f"Approximation: {APPROX_PI * calculate_parenthesis(terms)}")
    print(f"Terms used: {terms}")


if __name__ == "__main__":
    main()
