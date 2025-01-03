# Lab 6
# identity.py


def identity(n):
    for row in range(len(n)):
        for col in range(len(n[row])):
            n[row][col] = 0

    for i in range(len(n)):
        n[i][i] = 1
    return n


def main():
    print(identity([[100, 100, 100],
                    [100, 100, 100]]))  # should print [[1, 0, 0], [0, 1, 0]]
    print(identity([[100, 100, 100],
                    [100, 100, 100],
                    [100, 100, 100]]))  # should print [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


if __name__ == '__main__':
    main()
