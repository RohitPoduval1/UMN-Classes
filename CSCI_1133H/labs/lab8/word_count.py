# Lab 8


def word_count(fname):
    count = 0
    with open(fname, "r") as f:
        for line in f:
            for word in line.split(" "):
                count += 1
    return count


def main():
    print(word_count("testing.txt"))  # should print 4


if __name__ == "__main__":
    main()
