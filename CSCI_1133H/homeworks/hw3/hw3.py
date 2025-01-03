# Rohit Poduval, poduv006
# hw3.py
# hw3


#==========================================
# Purpose: remove D, F, and W from a list and create a new list with these values removed and the number of D, F, and Ws
# Input Parameters: a list of strings
# Return Value: a new list containing the number of strings with the value
# "D", "W", "F" and a list within that list of all the strings that are not "D", "F", or "W"
#==========================================
def remove_grades(mylist):
    new_list = []
    dfw_count = 0
    for grade in mylist:
        if grade.lower() != "d" and grade.lower() != "w" and grade.lower() != "f":
            new_list.append(grade)
        else:
            dfw_count += 1
    return [dfw_count, new_list]
    

#==========================================
# Purpose: calculate the average of only integers given a list of all types of data
# Input Parameters: a list containing different types of objects including ints
# Return Value: a list containing [count of ints, average of the ints, [list of the ints]]
#==========================================
def avg_ints(list):
    int_count = 0
    int_total = 0
    int_list = []

    for item in list:
        if type(item) == int:
            int_count += 1
            int_total += item
            int_list.append(item)

    if int_count == 0:  # cover the case where there are no ints in the list
        return [int_count, 0, int_list]  # in which case the average is zero
    else:
        return [int_count, int(int_total / int_count), int_list]


#==========================================
# Purpose: Find the minimums of each list within a list of numbers and the absolute minimum of the minimums
# Input Parameters: a list of lists of either numerical values or empty lists
# Return Value: a list of the minimums and the absolute minimum
    # [[minimums of each list], absolute minimum]
#==========================================
def all_minimums(lists):
    list_mins = []

    for list in lists:
        if len(list) == 0:  # if the list is empty, the minimum is 0
            list_min = 0
        else:
            list_min = list[0]  # have the list minimum start at the first position to make sure that a value 
            for num in list:    # that is not in the list is not set as the minimum value (i.e. a list of all negative numbers cannot have 0 as the min)
                if num < list_min:
                    list_min = num
        list_mins.append(list_min)
    
    if len(list_mins) == 0:
        absolute_min = 0
    else:
        absolute_min = list_mins[0]
    for min in list_mins:
        if min < absolute_min:
            absolute_min = min
    return [list_mins, absolute_min]


#==========================================
'''
Purpose: TODO
Input Parameters:
    -a list of ints, floats, and/or strings
    -numeric value to compare against
Return Value
    -True if the list contains elements that are all less than the value, False otherwise
    -If only strings are present in the list, False is returned
'''
#==========================================
def lesser_than(list, compare_value):
    is_all_strings = True  # assume initially that the list is all strings
    for item in list:
        if type(item) == int:
            is_all_strings = False  # if a number is present, then the is_all_strings becomes False
            if item > compare_value:  # if even one number in the list is greater than the given value, False is returned
                return False
    return (not(is_all_strings))  # if this return statement is hit, then all numbers were less than the given value
                                  # but the list must also be not all strings


#==========================================
# Purpose: sort a list of integers in ascending order of value starting at the back of the list
# Input Parameter: a list of integers
# Return Value: the inputed list of integers sorted in ascending order of value
    # (if my_list is passed in, my_list will be modified)
#==========================================
def selection_sort(list):
    if len(list) == 0 or len(list) == 1:  # cover edge cases
        return list
    else:
        largest = list[0]
        i = len(list) - 1
        index_of_largest_num = 0

        while i >= 0:
            for index, num in enumerate(list[0:(i+1)]):  # use a slice of the list cutting off the last element each time
                if num > largest:                        # since that element is guaranteed to be the largest in the list slice
                    largest = num
                    index_of_largest_num = index

            # move the largest element of the sliced list to the end of the sliced list
            # and move the value that was at the end to where the largest element was
            temp = list[i]
            list[i] = largest
            list[index_of_largest_num] = temp

            largest = -99999999999999999999999  # set to some arbitrarily large value so it does not obstruct the algorithm
            i -= 1  # reduce the size of the list slice by 1 each iteration
        return list


def main():
    # Tests for Problem 1
    print(remove_grades(["D", "F", "A", "A", "B", "W"]) == [3, ["A", "A", "B"]])
    print(remove_grades([]) == [0, []])  
    
    # Tests for Problem 2
    print(avg_ints([1, 2, 4, "sadie", 4.4, "bottle", 7.7]) == [3, 2, [1, 2, 4]])
    print(avg_ints([]) == [0, 0, []])

    # Test for Problem 3
    print(all_minimums([[1, 0, 5], [2, 3], [0, -1, 3]]) == [[0, 2, -1], -1])
    print(all_minimums([[], [1, 1, 1], []])  == [[0, 1, 0], 0])

    # Tests for Problem 4
    print(lesser_than([4, 4, 5.2, 6, "cat", "dog", 7.9, 8], 10) == True)
    print(lesser_than([], 3) == False)
    print(lesser_than([1,2,3], 2) == False)

    # Tests for Problem 5
    print(selection_sort([3, 2, 1, 4, 0]) == [0, 1, 2, 3, 4])
    print(selection_sort([3, 5, 2, 8, 9, 1]) == [1, 2, 3, 5, 8, 9])
    print(selection_sort([]) == [])


if __name__ == "__main__":
    main()
