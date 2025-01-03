# Lab 7
# translate.py

from string import punctuation


vowels = ["a", "e", "i", "o", "u"]


# Purpose: move beginning consonants to the end while removing any punctuation present
# Input Parameters: string (the word)
# Returns: the manipulated string in all lowercase
def move_beginning_consonants_to_end(word):
    beginning_consonants = ""

    # remove any punctuation present in "word"
    for punct in punctuation:
        word = word.replace(punct, "")

    # get the first consecutive consonants from "word"
    for letter in word:
        if letter.lower() not in vowels:
            beginning_consonants += letter.lower()
        else:
            break
        
    word_as_list = list(word)
    del word_as_list[:len(beginning_consonants)]  # remove the first beginning_consonants number of characters from the start of the string
    return str.join("", word_as_list) + beginning_consonants

# Purpose: return all indices of capital letters present in a string
# Input Parameter: string (a word)
# Return Value: ist (containing all indexes of capital letters)
def index_of_capital(word):
    capital_indexes = []
    for index, character in enumerate(word):
        if character.upper() == character and character.isalpha():
            capital_indexes.append(index)
    return capital_indexes
            

# Determine if/where punctuation is in a string
# Input Parameter: string (a word) 
# Return Value: list [either -1(no punctuation) or an index, the punctuation character]
def index_of_punctuation(word):
    index_punct = [-1, ""]
    for index, character in enumerate(word):
        if character in punctuation:
            index_punct = [index, character]
    return index_punct 

# Purpose: translate english to pig latin
# Input: text to translate
# Return: the pig latin translation
def eng_to_pig_latin(text):
    translated = ""

    for word in text.split(" "):
        ls = list(move_beginning_consonants_to_end(word))

        # make all the letters that were originally capitalized capital in the mixed up word
        for i in index_of_capital(word):
            ls[i] = ls[i].upper()  
        
        # the word starts with a consonant
        if word[0].lower() not in vowels:  
            
            # return the punctuation to the original place
            # input of "latin?" would return "atinlay?"
            if (index_of_punctuation(word))[0] > 0:
                translated += ("".join(ls) + "ay" + (index_of_punctuation(word))[1] + " ")
            else:
                translated += ("".join(ls) + "ay ")

        # the word starts with a vowel
        else:
            # return the punctuation to the original place
            # input of "latin?" would return "atinlay?"
            if (index_of_punctuation(word))[0] > 0:
                translated += ("".join(ls) + "way" + (index_of_punctuation(word))[1])
            else:
                translated += ("".join(ls) + "way ")

    return translated.strip()


def main():
    print(move_beginning_consonants_to_end("latin?") == "atinl")
    print(move_beginning_consonants_to_end("Can") == "anc")
    print(move_beginning_consonants_to_end("away") == "away")

    print(index_of_capital("hello") == [])
    print(index_of_capital("Piggies") == [0])
    print(index_of_capital("ComPuter?") == [0, 3])

    print(index_of_punctuation("") == [-1, ""])
    print(index_of_punctuation("Hello.") == [5, "."])

    print(eng_to_pig_latin("Can you speak pig latin?") == "Ancay ouyay eakspay igpay atinlay?")
    print(eng_to_pig_latin("An apple a day, keeps the doctor away.") == "Anway appleway away ayday, eepskay ethay octorday awayway.")


if __name__ == "__main__":
    main()
