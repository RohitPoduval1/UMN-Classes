# Rohit Poduval, poduv006
# tree.py
# HW2


# Purpose: get a yes or no answer to a question
# Input Parameter: message is the question that is shown to the user
# Return Value: "yes" or "no" entered by the user
def get_yes_or_no(message):
    while True:
        try:
            answer = input(message).lower()
            if answer != "yes" and answer != "no":
                raise ValueError
        except ValueError:
            print("Invalid input, enter yes or no")
        else:
            return answer

        
# Purpose: given answers to questions about the temperature, wind, and pressure, output whether it will rain or not 
# Return Value: whether it will rain or not indicated by "Rain" or "No rain"
def tree():
    temp_condition = get_yes_or_no("Is the temperature greater than 75 degrees Fahrenheit, yes or no?  ")
    if temp_condition == "yes":
        wind_condition_2 = get_yes_or_no("Is the wind speed greater than 2 miles per hour, yes or no?  ")
        if wind_condition_2 == "yes":
            pressure_condition_24 = get_yes_or_no("Is the pressue greater than 24 inHg, yes or no?  ")
            if pressure_condition_24 == "yes":
                return "Rain"
            elif pressure_condition_24 == "no":
                return "No rain"
        elif wind_condition_2 == "no":
            return "No rain"
    elif temp_condition == "no":
        wind_condition_6 = get_yes_or_no("Is the wind speed greater than 6 miles per hour, yes or no?  ")
        if wind_condition_6 == "yes":
            return "Rain"
        elif wind_condition_6 == "no":
            pressure_condition_31 = get_yes_or_no("Is the pressue greater than 31 inHg, yes or no?  ")
            if pressure_condition_31 == "yes":
                return "Rain"
            elif pressure_condition_31 == "no":
                return "No rain"


def main():
    print(tree())


if __name__ == "__main__":
    main()
