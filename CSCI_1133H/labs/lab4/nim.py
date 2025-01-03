import random


# Lab 4

# Rules:
# 2 players alternate removing 1, 2, or 3 objects from 21 objects
# Player who plays last wins

# returns a string of either "y" for going first or "n" for not choosing to go first
def get_choice():
    choice = input("Would you like to go first (y/n)? ").lower()
    
    while choice != "y" and choice != "n":
        print("Invalid input, enter 'y' for yes or 'n' for no")
        choice = input("Would you like to go first (y/n)? ").lower()
        
    return choice


# returns a number between 1 and 3 inclusive as the player's move
def get_number():
    num = int(input("Do you want to take 1, 2, or 3: "))
    while num > 3 or num < 1:
        print("Enter a number between 1 and 3 inclusive")
        num = int(input("Do you want to take 1, 2, or 3: "))
    return num

        
def main():
    choice = get_choice()

    remaining_objects = 21
    while remaining_objects > 0:
        
        if choice == "n":
            if 1 <= remaining_objects <= 3:  # it is possible for the computer to win in
                my_turn = remaining_objects  # in this situation
                remaining_objects -= my_turn
            if remaining_objects == 0:
                print("I win!")
            elif remaining_objects > 3:          # if there are more than 3, it is
                my_turn = random.randint(1, 3)   # not possible for the computer to win so
                remaining_objects -= my_turn     # it must make a random move
                print(f"I'll take {my_turn}")
                print(f"{remaining_objects} objects remain.")
            choice = "y"  # alternating moves is made possible by altering the choice variable
            
        elif choice == "y":
            your_turn = get_number()
            while remaining_objects - your_turn < 0:
                print("Invalid move, go again")
                your_turn = get_number()
            remaining_objects -= your_turn
            print(f"{remaining_objects} objects remain")
            if remaining_objects == 0:
                print("You win!")
            choice = "n"


if __name__ == "__main__":
    main()
    
