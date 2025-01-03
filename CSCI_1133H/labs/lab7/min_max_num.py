# Lab 7
# min_max_num.py

# Purpose: Return the length of the minimum and maximum strings in a sentence
# Input: a string (sentence)
# Returns: list [minimum size, maximum size]
def min_max_nums(words):
    words = words.split(" ")
    min_size = len(words[0])
    max_size = len(words[0])
    for word in words:
        if len(word) < min_size:
            min_size = len(word)
        elif len(word) > max_size:
            max_size = len(word)
    return [min_size, max_size]


def main():
    print(min_max_nums("The yellow kite was flying in the bright blue sky") == [2, 6])
    print(min_max_nums("") == [0, 0])
    print(min_max_nums("hi") == [2, 2])


if __name__ == "__main__":
    main()
