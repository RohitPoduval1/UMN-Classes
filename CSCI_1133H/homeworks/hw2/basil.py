# Rohit Poduval, poduv006
# basil.py
# HW2


# Purpose: calculates pounds to kilograms
# Input Parameter: weight in pounds
# Return Value: weight as kilograms (float)
def convert_pounds_to_kg(pounds):
    return pounds * 0.453592


# Purpose: calculates inches to centimeters
# Input Parameter: length in inches
# Return Value: length as centimeters (float)
def convert_inches_to_cm(inches):
    return inches * 2.54


# Purpose: calculates the Harris and Benedict BMR
# Input Parameters
    # weight: the wieght of the person in kg
    # height: the height of the person in cm
    # age: the age of the person in years (integer values only)
    # gender: the gender of the person (use "f" for female and "m" for male)
# Return Value: basal metabolic rate as a float
def h_and_b(weight, height, age, gender):
    if gender == "f":
        return 655.1 + (9.563 * weight) + (1.85 * height) - (4.676  * age)
    elif gender == "m":
        return 66.5 + (13.75 * weight) + (5.003 * height) - (6.755  * age)


# Purpose: calculates the Roza and Shizgal BMR
# Input Parameters
    # weight: the wieght of the person in kg
    # height: the height of the person in cm
    # age: the age of the person in years (integer values only)
    # gender: the gender of the person (use "f" for female and "m" for male)
# Return Value: basal metabolic rate as a float
def r_and_s(weight, height, age, gender):
    if gender == "f":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.33  * age)
    elif gender == "m":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677  * age)


# Purpose: calculates the Millflin and St Jeor BMR
# Input Parameters
    # weight: the wieght of the person in kg
    # height: the height of the person in cm
    # age: the age of the person in years (integer values only)
    # gender: the gender of the person (use "f" for female and "m" for male)
# Return Value: basal metabolic rate as a float
def m_and_s(weight, height, age, gender):
    if gender == "f":
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    elif gender == "m":
        return (10 * weight) + (6.25 * height) - (5  * age) + 5


# Purpose: get an integer for the variable age while prompting the user to input an integer
# Return Value: the value for the variable age
def get_age():
    while True:
        try:
            age = int(input("Your current age: "))
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return age


# Purpose: get an integer for the variable weight while prompting the user to input an integer
# Return Value: the value for the variable weight
def get_weight():
    while True:
        try:
            weight = float(input("Your weight (in pounds):  "))
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return weight


# Purpose: get an integer for the variable height while prompting the user to input an integer
# Return Value: the value for the variable height
def get_height():
    while True:
        try:
            height = round(float(input("Your height (in inches):  ")), 1)
        except ValueError:
            print("Invalid input, enter a number")
        else:
            return height


# Purpose: get a specific for the variable gender while prompting the user to input an integer
# Return Value: the value for the variable gender (either "f" for female or "m" for male)
def get_gender():
    while True:
        try:
            gender = input("Your gender: ").lower()
            if gender != "f" and gender != "m":
                raise ValueError
        except ValueError:
            print("Invalid input, enter 'f' for female or 'm' for male")
        else:
            return gender

        
def main():
    age = get_age()
    gender = get_gender()
    weight = get_weight()
    height = get_height()

    print()
    print(f"Your weight in kilograms: {round(convert_pounds_to_kg(weight), 1)}")
    print(f"Your height in centimeters: {round(convert_inches_to_cm(height), 1)}")
    print(f"Harris and Benedict BMR: {round(h_and_b(weight, height, age, gender), 1)}")
    print(f"Roza and Shizgal BMR: {round(r_and_s(weight, height, age, gender), 1)}")
    print(f"Mifflin and St Jeor BMR: {round(m_and_s(weight, height, age, gender), 1)}")


if __name__ == "__main__":
    main()
