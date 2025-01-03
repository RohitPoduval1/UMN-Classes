# Lab 6
# remove_punc.py

# Purpose: remove given punctuation from a string
# Input Parameters: text (in the form of a string) and punctuation to be removed (in the form of a string)
# Return: the text with the given punctuation removed
def remove_punc(text, punc):
    for punctuation_mark in punc:
        text = text.replace(punctuation_mark, "")
    return text


def main():
    print(remove_punc('Rem!ove, o?nly th3 exc!amati.n points!', '!') == 'Remove, o?nly th3 excamati.n points')
    print(remove_punc('??Ge!t r;!;id of m,o,s,t punctuation', '.!;,?') == 'Get rid of most punctuation')


if __name__ == '__main__':
    main()
    