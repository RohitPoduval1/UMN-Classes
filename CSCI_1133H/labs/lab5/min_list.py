# Lab 5
# min_list.py

'''
Input Parameters:
    -int_list is a list of nonnegative integers
    -starting_index is the starting index of the int_list to start searching for a minimum value
Return Value: the index of the minimum value within the range of starting_index to the end of the list
'''
def minimum_index(int_list, starting_index):
    current_min = int_list[starting_index]
    for i in range(starting_index, len(int_list)):
        if int_list[i] < current_min:
            current_min = int_list[i]
    
    for i in range(len(int_list)):
        if int_list[i] == current_min:
            return i

print(minimum_index([9, 1, 7, 6, 8], 2))
