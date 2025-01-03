# Lab 5
# hist.py
# Simulates the tossing of two dice and keep track of the occurrence
# frequency of each two-dice sum (2...12)


import random


num_pairs = 10000
sums = []

for i in range(num_pairs):
    sums.append(random.randint(1, 6) + random.randint(1, 6))

for i in range(2, 13):
    print(f"{i}: {format(sums.count(i), '5d')}")
