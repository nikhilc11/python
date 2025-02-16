#######################################################################################################################
#
# Check if an array contains all elements of a given range
#
# An array containing positive elements is given.
# ‘A’ and ‘B’ are two numbers defining a range.
# Write a function to check if the array contains all elements in the given range.
#
# Examples :
#
# Input : arr[] = {1 4 5 2 7 8 3}
#            A : 2, B : 5
# Output : Yes
# Input : arr[] = {1 4 5 2 7 8 3}
#           A : 2, B : 6
# Output : No
#######################################################################################################################

#######################################################################################################################
# Approach - index flag approach
#######################################################################################################################

def check_elements_in_range(array, lower_bound, higher_bound):
    flag_array = [0] * (higher_bound-lower_bound+1)
    for element in array:
        if lower_bound <= element <= higher_bound:
            flag_array[element-lower_bound] = 1
    if sum(flag_array) == len(flag_array):
        return True
    else:
        return False


arr = [1, 4, 5, 2, 7, 8, 3]
A, B = 2, 5
print(check_elements_in_range(arr, A, B))

#######################################################################################################################
