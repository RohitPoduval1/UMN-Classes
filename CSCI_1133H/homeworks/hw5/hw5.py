# Rohit Poduval, poduv006
# hw5.py
# HW5


#==========================================
# Purpose: produces a list of numbers in the sequence (base^0, base^1, base^2, base^3, ..., base^n)
# Input Parameter(s):
    # n is an integer that represent the exponent of (n >= 0 and is an integer)
    # base is the base of the number (base > 0 and is an integer)
# Return Value(s):
    # returns a list of numbers {base^0, base^1, base^2, base^3, ..., base^n}
#==========================================
def base_seq(n, base): 
    if n == 0:  # base case 
        return [1]
    else:
        return base_seq(n-1, base) + [base ** n]


#==========================================
# Purpose: find how many things in the list are not numbers 
# Input Parameter(s): a list of items containing...
    # numbers (i.e. float, int, complex)
    # strings
    # tuples
    # lists
# Return Value(s): returns the count of the things in the list that are not numbers
#==========================================
def cnt_non_num(input_list):
    if len(input_list) == 0:  # base case (the length of input_list keeps on decreasing until its 0)
        return 0
    
    elif type(input_list[0]) == tuple or type(input_list[0]) == list:
        return 1 + cnt_non_num(input_list[0]) + cnt_non_num(input_list[1:])
        # add 1 since collections of data aren't numbers
        # since it is a collection of data, the program must check the nested collection for any non numbers
    
    elif type(input_list[0]) == int or type(input_list[0]) == float or type(input_list[0]) == complex:
        return cnt_non_num(input_list[1:])
        # add nothing since it is a number
        # trim the list, ignoring that numeric value

    elif type(input_list[0]) == str:
        return 1 + cnt_non_num(input_list[1:])
        # add 1 since a string is not a number
        # trim the list since the string has just been accounted for
    

#==========================================
# Purpose: Find the minimum and maximum hours worked per week for each employee given
# Input Parameter(s): a dictionary containing pairs of employee names and hours worked per week
# Return Value(s): returns a new dictionary with keys representing employees and a list of their
# [min number of hours worked, max number of hours worked]
#========================================== 
def min_max(emp_hours):
    new_dict = {}
    if emp_hours == {}:
        return {}
    else:
        for person_name in emp_hours.keys():
            if emp_hours[person_name] == []:    # if the person hasn't worked,
                new_dict[person_name] = [0, 0]  # then their min and max is 0
            else:                               # if they have worked, 
                new_dict[person_name] = [min(emp_hours[person_name]), max(emp_hours[person_name])]  # then find the min and max of the hours they worked
    return new_dict


def main():
    print(base_seq(2, 2) == [1, 2, 4])
    print(base_seq(0, 2) == [1])
    print(base_seq(1, 5) == [1, 5])
    print(base_seq(4, 4) == [1, 4, 16, 64, 256])
    print(base_seq(10, 2) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

    print(cnt_non_num([1, 2, 3, 'abc', 5.5, [1, [2, 3, ("a", "b","c")]]]) == 7)
    print(cnt_non_num([]) == 0)
    print(cnt_non_num(["dog", "cat", "b", ["flower", 3.2, complex(5,4)]]) == 5)
    print(cnt_non_num([0, 99, 8.5]) == 0)
    print(cnt_non_num([0, 99, complex(1,1),[]]) == 1)
    print(cnt_non_num([[], [[]]]) == 3)

    print(min_max({"Shana": [20], "Jody": [10, 20, 10, 5], "Mike":[40, 40]}) == {'Shana': [20, 20], 'Jody': [5, 20], 'Mike': [40, 40]})
    print(min_max({"Shana": [20, 20, 20, 60, 70, 5], "Ahmed": [40, 50,10]}) == {"Ahmed": [10, 50], "Shana": [5, 70]})
    print(min_max({}) == {})
    print(min_max({"Marty": []}) == {'Marty': [0,0]})

if __name__ == "__main__":
    main()
