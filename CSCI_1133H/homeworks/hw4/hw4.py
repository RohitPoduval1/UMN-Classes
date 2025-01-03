# Rohit Poduval, poduv006
# hw4.py
# HW4


#==========================================
# Purpose: given a string, this function returns string with its first character capitalized and the rest lowercased
# Input Parameter(s): takes in a string 
# Return Value(s):
    # returns a string with its first character capitalized and the rest lowercased
    # if a character cannot be capitalized or lowercased, the character is unchanged
#==========================================
def str_capitalize(my_str):
    if len(my_str) > 0:
        new_str = (my_str[0]).upper()
        for character in my_str[1:]:        # skip the first character since it has already been capitalized
            new_str += character.lower()    # make the rest lowercase
        return new_str
    else:
        return ""
     

#==========================================
# Purpose: counts the number of non-overlapping occurrences of the substring sub in the string
# Input Parameter(s): takes in 2 strings
    # the main string to look into
    # the substring to look for
# Return Value(s):
    # returns the number of times the substring was found in the string
    # If sub is empty, the function returns the number of empty strings between characters which is the length of the my_str plus one
#==========================================
def str_count(my_str, sub):
    if len(sub) == 0:
        return len(my_str) + 1
    else:
        i = 0
        count = 0
        while  i < len(my_str) - len(sub) + 1:  # "sub" cannot be found if there are not enough characters at the end of "my_str"
            if my_str[i:i+len(sub)] == sub:  # check if the sequence of characters the length of "sub" matches "sub"
                count += 1                   # you already knows what comes next if the sequence matches
                i += len(sub)                # so skip over the part you know
            else:
                i += 1
        return count


#==========================================
# Purpose: find the first occurence of a substring within a string
# Input Parameter(s): takes in 2 strings
    # the main string to look into
    # the substring to look for
# Return Value(s):
    # return the index position where the first occurrence of val is found in my_str.
    # if val is not found, return -1
#==========================================
def str_find(my_str, val):
    i  = 0
    while i < len(my_str) - len(val) + 1:
        if my_str[i:i+len(val)] == val:
            return i
        else:
            i += 1
    return -1


#==========================================
# Purpose: find the first occurence of a substring within a string
# Input Parameter(s):
    # my_str: A string
    # val: A value to search for
    # start: optional, defaults to 0, where in my_str to start the search
    # end: optional, defaults to end of the my_str, where in my_str to end the search
# Return Value(s):
    # return the index position where the first occurrence of val is found in my_str (or the substring given optional inputs).
    # if val is not found, return -1
#==========================================
def str_find2(my_str, val, start=0, end=-999999991):
    if end == -999999991 or end > len(my_str):  # this means end either defaulted or exceded the length of my_str, in which case,
        end=len(my_str)    # set end to be the length of my_str to avoid unnecessary looping
    
    i = start
    while i <= end - len(val) + 1:  # (+1 makes function inclusive of endpoint)
        if my_str[i : i+len(val)] == val:
            return i
        else:
            i += 1
    return -1




#==========================================
# Purpose: check if a string is alphanumeric 
# Input Parameter: my_str: A string
# Return Value(s): Return True if all characters in my_str are alphanumeric and there is at least one character, return False otherwise
#==========================================
def str_isalnum(my_str):
    if len(my_str) == 0:
        return False
    for char in my_str:
        if not (char.isalpha() or char.isdecimal() or char.isdigit() or char.isnumeric()):
            return False
    return True


#==========================================
# Purpose: insert my_str after each character in str_iter except the last
# Input Parameters:
    # my_str: str to insert (is repeated in the final string)
    # str_iter: unique string that is added to
# Return Value(s): returns str_iter with my_str inserted after each character except the last character (the variable str_iter is not modified)
#==========================================
def str_join(my_str, str_iter):
    if len(my_str) == 0:
        return str_iter
    else:
        final_string = ""
        for char in str_iter[0:-1]:  # don't insert anything after the last character
            final_string += (char + my_str)
        return final_string + str_iter[-1]


#==========================================
# Purpose: interleave to strings then remove any numbers within that interleaved string
# Input Parameters: two strings to be interleaved
    # s1: a string
    # s2: a string
# Return Value(s): returns s1 interleaved with s2; this interleaved string will have any numbers in it removed 
#==========================================
def rm_num_combine(s1, s2):
    interleaved_string_with_numbers = ""
    '''
    The general algorithm of the function
        1. Loop through the shorter string
        2. Append to an empty string variable the first character of s1 and the first character s2
        3. Repeat #2 until we reach the end of the shorter string
        4. Append the rest of the characters of the longer string (that haven't been reached yet) to the string variable containing the interleaved characters
        5. Loop through that interleaved string and remove any characters that are numbers
        6. Return that string in #5
    '''
    if len(s1) > len(s2):
        for i in range(len(s2)):
            interleaved_string_with_numbers += (s1[i] + s2[i])
        interleaved_string_with_numbers += s1[len(s2):]
        final_str = ""
        for char in interleaved_string_with_numbers:
            if not char.isdigit():
                final_str += char
    elif len(s2) > len(s1):
        for i in range(len(s1)):
            interleaved_string_with_numbers += (s1[i] + s2[i])
        interleaved_string_with_numbers += s2[len(s1):]
        final_str = ""
        for char in interleaved_string_with_numbers:
            if not char.isdigit():
                final_str += char
    else:
        for i in range(len(s1)):
            interleaved_string_with_numbers += (s1[i] + s2[i])
        final_str = ""
        for char in interleaved_string_with_numbers:
            if not char.isdigit():
                final_str += char
    return final_str



def main():    
    print(str_capitalize("heAAB") == "Heaab")
    print(str_capitalize("123heAAB") == "123heaab")
    print(str_capitalize("#$$$233") == "#$$$233")
    print(str_capitalize("$UPer Job!!")  == "$uper job!!")
    print(str_capitalize("") == "")
    print(str_capitalize("ab") == "Ab")
    
    print(str_count("aaaabbbbb", "aa") == 2)
    print(str_count("aaaabbbbb", "") == 10)
    print(str_count("", "") == 1)
    print(str_count("aaabaaab", "aa") == 2)
    print(str_count("aaccaaccaacc", "cc") == 3)
    
    print(str_find("aaacbaabb", "dd") == -1)
    print(str_find("","") == 0)
    print(str_find("aa", "") == 0)
    print(str_find("aaabaaabbbb", "bb") == 7)

    # inclusive or exclusive?
    print(str_find2("aaabaaabbbb", "bb", 5, 12) == 7)
    print(f'{str_find2("aaabaaabbbb", "bb", 0, 1) == -1}')
    print(str_find2( "aaabaaabbbb", "", 5, 9) == 5)
    print(str_find2("BBBBB", "A") == -1)
    print(f"{str_find2('aaabaaabbbb', 'b', 5) == 7}")
    print(f"{str_find2('aabbaaccd', 'aa', 0, 6) == 0}")
    print(f"{str_find2('bbb', 'bbb', 0, 2)} EDGE CASE")
    

    print(str_isalnum("123abc") == True)
    print(str_isalnum("123abc#") == False)    
    print(str_isalnum("") == False)    
    print(str_isalnum("!") == False)    
    print(str_isalnum("1a") == True)    

    print(str_join("123", "abc") == 'a123b123c')
    print(str_join("1", "abc") == 'a1b1c')
    print(str_join("", "abc") == "abc")
    print(str_join("", "") == "")
    print(str_join("", "hello") == "hello")
    
    print(rm_num_combine("a1c", "mn2z") == "amncz")
    print(rm_num_combine("", "") == "")
    print(rm_num_combine("123", "456") == "")
    print(rm_num_combine("123a", "456") == "a")


if __name__ == "__main__":
    main()