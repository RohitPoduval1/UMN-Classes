# Lab 11
# Workout


def flat_deep_square(ls):
    if len(ls) == 0:
        return []
    elif type(ls[0]) == list:
        return flat_deep_square(ls[0]) + flat_deep_square(ls[1:])
    elif type(ls[0]) == int:
        return [ls[0] ** 2] + flat_deep_square(ls[1:])


def main():
    print(flat_deep_square([[-1,[2],[3],[[[-4,5]]],[],[]]]) == [1,4,9,16,25])



if  __name__ == '__main__':
    main()