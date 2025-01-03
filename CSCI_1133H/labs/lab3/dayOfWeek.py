number_day = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def day_of_week(month, day, year):
    if month == 1:
        return number_day[(day + 5 + ((26 * (13+1)) // 10) + ((5 * (year%100)) // 4) + ((21 * (year // 100)) // 4)) % 7]
    elif month == 2:
        return number_day[(day + 5 + ((26 * (14+1)) // 10) + ((5 * (year%100)) // 4) + ((21 * (year // 100)) // 4)) % 7]
    else:
        return number_day[(day + 5 + ((26 * (month+1)) // 10) + ((5 * (year%100)) // 4) + ((21 * (year // 100)) // 4)) % 7]


def main():
    year = int(input("Enter a year in numerical format: "))
    month = int(input("Enter a month in numerical format: "))
    day = int(input("Enter a day of the month in numerical format: "))

    # Processes the modified months of January and February under the hood
    # so the user can enter the date they want and the program will modify the
    # month and year values manually
    if month == 1:
        year -= 1
        
    print(day_of_week(month, day, year))


if __name__ == "__main__":
    main()
            
