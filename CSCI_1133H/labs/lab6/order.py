# Lab 6
# order.py
# DONE: Double check

# returns number of rows times number of columns of a square matrix
def order(m):
    return len(m) ** 2  # in a square matrix, the rows are equal to the number of columns


def main():
    print(order(
        [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 2, 2, 1],
        [1, 1, 1, 1]]))  # should print 16


if __name__ == "__main__":
    main()
