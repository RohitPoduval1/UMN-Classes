# Lab 10
# morse_code.py


morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}


# Purpose: convert an UPPERCASE string to morse code symbols
# Input Parameters: the message to convert in uppercase (cannot contain special characters, only letters and spaces)
# Return: the morse code translation for the message
def convert_to_morse_code(message):
    morse_translation = ""

    for character in message:
        morse_translation += (morse_dictionary[character] + " ")
    
    return morse_translation


def main():
    message = input("Enter a message: ")
    message = message.upper()

    print(convert_to_morse_code(message))

if __name__ == '__main__':
    main()