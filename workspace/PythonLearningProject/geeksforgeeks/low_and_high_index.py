#######################################################################################################################
#
# Given an array of integers arr sorted in ascending order,
# find the starting and ending position of a given target value (key).
# If the target is not found in the array, return [-1, -1].
#
# Examples:
# Input: arr = [5, 7, 7, 8, 8, 10], key = 8
# Output: [3, 4]
#
#######################################################################################################################

#######################################################################################################################
# Approach -
#######################################################################################################################

def binary_search(arr, search_key, start, end):
    while start <= end:

        mid = start + (end - start) // 2

        if search_key < arr[mid]:
            end = mid - 1
        elif search_key > arr[mid]:
            start = mid + 1
        else:
            return mid

    return -1

def find_index_high_and_low_for_key(arr, key):
    low_index, high_index = 0, 1

    while (key > arr[high_index]):
        temp = high_index + 1
        high_index = high_index + (high_index - low_index + 1) * 2
        low_index = temp

    return binary_search(arr, key, low_index, high_index)

pos = find_index_high_and_low_for_key([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6], 4)

print(pos)

#######################################################################################################################
