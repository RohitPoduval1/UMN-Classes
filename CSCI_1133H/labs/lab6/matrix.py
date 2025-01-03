# Lab 6
# matrix.py


def matrix(n, init_value):
    m = []
    row_list = []
    for row in range(n):
        for col in range(n):
            row_list.append(init_value)
        m.append(row_list)
        row_list = []

    return m


def main():
    print(matrix(4, 1))


if __name__ == '__main__':
    main()