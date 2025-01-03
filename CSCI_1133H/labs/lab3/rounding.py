def round_float(floating_value):
    if floating_value >= 0:  
        return int(floating_value + 0.5)
    else:
        return int(floating_value - 0.5)


def main():
    num = float(input("Enter a floating point number: "))
    print(f"The rounded integer is {round_float(num)}")


if __name__ == "__main__":
    main()
