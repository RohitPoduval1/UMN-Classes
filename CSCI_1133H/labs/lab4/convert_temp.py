# Lab 4
# Finds a temperature that is the same in both fahrenheit and celsius


c = 100  # temperature in celsius
f = (9/5) * c + 32  # temperature in fahrenheit


while f != c:  # keep checking to see if fahrenheit and celsius temps are equal
    c -= 1     # exit the while loop if they are
    f = (9/5) * c + 32


print(f"The temperature that is the same in both celsius and fahrenheit is {c} degrees")
