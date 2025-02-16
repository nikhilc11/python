#######################################################################################################################
# Given an array arr[] where no two adjacent elements are same, find the index of a peak element.
# An element is considered to be a peak element if it is strictly greater than its adjacent elements.
# If there are multiple peak elements, return the index of any one of them.
#
# Note: Consider the element before the first element and the element after the last element to be negative infinity.
#
# Examples:
#
# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 5
# Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
#
#
# Input: arr[] = [10, 20, 15, 2, 23, 90, 80]
# Output: 1 or 5
# Explanation: arr[1] = 20 and arr[5] = 90 are peak elements
# because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6].
#
#
# Input: arr[] = [1, 2, 3]
# Output: 2
# Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element,
# so it has negative infinity to its right.
#######################################################################################################################

#######################################################################################################################
# Approach 1 - Position of max element
#######################################################################################################################

print("Approach 1 - Position of max element")

def find_max(arr) :
    max_element_pos = 0
    max_element = 0

    for i in range(0,len(arr)):
        if arr[i] > max_element:
            max_element_pos = i
            max_element = arr[i]

    return max_element_pos

# Assuming no negative values are there in the set of input values
print(find_max([1, 2, 4, 5, 7, 8, 3]))
print(find_max([10, 20, 15, 2, 23, 90, 80]))
print(find_max([1, 2, 3]))
print(find_max([3, 2, 1]))


#######################################################################################################################
# Approach 2 - Position of first peak
#######################################################################################################################

print("Approach 2 - Position of first peak")

def find_first_peak(arr) :
    peak_element_pos = -1
    pass

    for i in range(0,len(arr)):

        if i == 0 and arr[i] > arr [i+1]:
            peak_element_pos = i;
        elif i == len(arr) - 1 and arr[i - 1] < arr[i]:
            peak_element_pos = i;
        else:
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                peak_element_pos = i;

        if peak_element_pos != -1:
            break

    return peak_element_pos

# Assuming no negative values are there in the set of input values
print(find_first_peak([1, 2, 4, 5, 7, 8, 3]))
print(find_first_peak([10, 20, 15, 2, 23, 90, 80]))
print(find_first_peak([1, 2, 3]))
print(find_max([3, 2, 1]))

#######################################################################################################################
