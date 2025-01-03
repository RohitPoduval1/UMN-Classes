def gather_data(file_name):
    with open(file_name, 'r') as f:
        for num, category in enumerate((f.readline()).split(",")):
            print(f"{num} {category}")            


print(gather_data("2.5_day.csv"))



def show_useful_data(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.split(",")
            print(f"{line[4]} {line[14]}")

def main():
    show_useful_data("2.5_day.csv")

if __name__ == '__main__':
    main()
