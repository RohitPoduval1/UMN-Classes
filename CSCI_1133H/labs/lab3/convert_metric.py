conversions = {
    "pounds": 0.453592,
    "ounces": 28.3495,
    "miles": 1.60934, 
    "inches": 2.54,
    "kilograms": 2.20462,
    "grams": 0.035274,
    "kilometers": 0.621371,
    "centimeters": 0.392701 
}


def metric_conv(measurements, units):
    return measurements * conversions[units]


def main():
    measurement = float(input("Enter a measurement: "))
    units = input("Enter a unit: ")

    if units not in conversions.keys():
        raise Exception("Invalid unit")
        
    print(metric_conv(measurement, units))


if __name__ == "__main__":
    main()
