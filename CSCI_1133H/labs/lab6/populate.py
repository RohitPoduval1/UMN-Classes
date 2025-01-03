# Lab 6
# populate.py


from random import randint

# len(matrix) = number of rows
# len(matrix[i]) = number of columns
def populate(matrix, n, value):
    for i in range(n):  # generate n number of random values
        matrix[randint(0, len(matrix) - 1)][randint(0, len(matrix[0]) - 1)] = value               # choose random spots in the matrix to assign to value
    return matrix


def main():
    matrix = [
        [4, 4, 4],
        [4, 4, 4],
        [4, 4, 4]]

    print(populate(matrix, 0, 3))  # matrix is unchanged
    print(populate(matrix, 5, 3))  # 5 random positions are changed


if __name__ == '__main__':
    main()
