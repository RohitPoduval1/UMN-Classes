# Lab 7
# min_max_words.py


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


# Purpose: Return the words of the minimum and maximum length in a sentence
# Input: a string (sentence)
# Returns: list [minimum sized word, maximum sized word]
def min_max_words(text):
    words = text.split(" ")
    extreme_lengths = min_max_nums(text)
    min_words = []
    max_words = []

    if len(text) == 0:
        return [[], []]
    
    for word in words:
        if len(word) == extreme_lengths[0]:
            min_words.append(word)
        if len(word) == extreme_lengths[1]:
            max_words.append(word)
    return [min_words, max_words]


def main():
    print(min_max_words("The yellow kite was flying in the bright blue sky") == [["in"], ["yellow", "flying", "bright"]])
    print(min_max_words("") == [[], []])
    print(min_max_words("word") == [["word"], ["word"]])


if __name__ == "__main__":
    main()
    