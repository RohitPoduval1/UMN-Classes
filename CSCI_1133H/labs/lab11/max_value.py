# Lab 11
# Warm up 2


def max_value(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        if ls[0] < ls[1]:
            return max_value(ls[1:])
        else:
            del ls[1]
            return max_value(ls)


def main():
    print(max_value([1, 2, 3, 4]))
    print(max_value([1, 3, 5, 3, 4, 9, 1, 4]))


if __name__ == '__main__':
    main()