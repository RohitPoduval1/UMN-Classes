# Rohit Poduval, poduv006
# loop_for.py
# HW2

# Purpose: calculate the sum after subtracting "sub" from "total" "times" times
# Input Parameter: total is a given total to start with
# Input Parameter: sub is the number to subtract (can be negative)
# Input Parameter: times is the number of times to do the subtraction
# Return Value: sum after subtracting "sub" from "total" "times" times
# Ex. loop_for(30, 2, 5) = 28+26+24+22+20 = 120
def loop_for(total, sub, times):
    total_sum = 0
    for i in range(0, times):
        total -= sub
        total_sum += total
    return total_sum

# Purpose: get an integer for the variable total while prompting the user to input an integer
# Return Value: the value for the variable total
def get_total():
    while True:
        try:
            total = int(input("Please enter the current total:  "))
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return total

# Purpose: get an integer for the variable subtract_num while prompting the user to input an integer
# Return Value: the value for the variable subtract_num
def get_subtract_num():
    while True:
        try:
            subtract_num = int(input("What number will be subtracted?  "))
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return subtract_num

# Purpose: get an integer for the variable times while prompting the user to input an integer
# Return Value: the value for the variable times
def get_times():
    while True:
        try:
            times = int(input("How many times should we subtract?  "))
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return times


def main():
    total = get_total()
    subtract_num = get_subtract_num()
    times = get_times()

    print(f"Answer:  {loop_for(total, subtract_num, times)}")


if __name__ == "__main__":
    main()
