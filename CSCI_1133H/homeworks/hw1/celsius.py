# Rohit Poduval, poduv006
# celsius.py
# HW1


print("This program converts Celsius to Fahrenheit and Kelvin\n")
temp_c = float(input("Please enter the temperture in Celsius: "))

temp_f = int((9/5)*temp_c + 32)
print(f"The temperature in Fahrenheit is: {temp_f}")

temp_k = int(temp_c + 273.15)
print(f"The temperature in Kelvin is: {temp_k}")

if temp_f <= 32:
    print("It is cold!")
elif temp_f > 32 and temp_f < 70:
    print("It is cool.")
else:
    print("It is warm.")
