# Lab 5
# occurs.py
# Repeatedly prompts the user to enter a word (a string) and stores in a
# list only those words whose first letter occurs again elsewhere in the word


def contains_repeat_of_first_letter(word):
    for letter in word[1:]:
        if letter == word[0]:
            return True
        

valid_words = []
word = input("Insert word: ")
if contains_repeat_of_first_letter(word.lower()):
        valid_words.append(word)


while len(word) != 0:
    word = input("Insert word: ")
    if contains_repeat_of_first_letter(word.lower()):
        valid_words.append(word)


for valid_word in valid_words:
    print(valid_word)
