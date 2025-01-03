# Lab 8

from random import randint


def generate_100_random_lines(myfile):
    with open(myfile, "w") as f:
        for i in range(1, 101, 1):
            f.write(f"{i}, {randint(-1000, 1000)}\n")


def main():
    file_name = input("Input a name for the csv file (i.e. 'example.csv'): ")
    generate_100_random_lines(file_name)


if __name__ == "__main__":
    main()