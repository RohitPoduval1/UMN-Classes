# BMR.py


def calculate_bmr(weight, height, age, sex):
    if sex.upper() == "F":
        return 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    elif sex.upper() == "M":
        return 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    age = float(input("Enter your age in years: "))
    sex = input("Enter M for male or F for female: ")
    bmr = calculate_bmr(weight, height, age, sex)
    
    print(f"You need to eat {(bmr / 230):.2f} chocolate bars to maintain your weight")


if __name__ == "__main__":
    main()
    
