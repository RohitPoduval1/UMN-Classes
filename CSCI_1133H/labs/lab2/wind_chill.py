def compute_wind_chill():
    temp = float(input("Enter a temperature in Fahrenheit: "))
    if temp < -58 or temp > 41:
        print("The formula used only works with temperatures between -58 and 41 degrees Fahrenheit")
    else:
        wind_vel = float(input("Enter a wind velocity in miles per hour: "))
        print(35.74 + (0.6215*temp) - (35.75*(wind_vel**0.16)) + (0.4275*temp*(wind_vel**0.16)), "degrees Fahrenheit")
