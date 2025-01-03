# Lab 8


import os 

def find_min_max(file_name):
    current_min = 1001
    current_max = -1001

    if file_name not in os.listdir("/Users/rohitpoduval/Documents/GitHub/repo-poduv006/labs/lab8/"):
        return "Bad file name"
    else:
        with open(file_name, 'r') as f:    
            for line in f:
                if int(((line.split(","))[1]).strip()) < current_min:
                    current_min = int(((line.split(","))[1]).strip())
                if int(((line.split(","))[1]).strip()) > current_max:
                    current_max = int(((line.split(","))[1]).strip())

        return [current_min, current_max]


def main():
    file_name = input("Input a name for the csv file filled with random integers (i.e. 'example.csv'): ")
    print(find_min_max(file_name))

    
if __name__ == "__main__":
    main()