#######################################################################################################################
#
# Find position of an element in a sorted array of infinite numbers
#
# Given a sorted array arr[] of infinite numbers. The task is to search for an element k in the array.
#
# Examples:
#
# Input: arr[] = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], k = 10
# Output: 4
# Explanation: 10 is at index 4 in array.
#
# Input: arr[] = [2, 5, 7, 9], k = 3
# Output: -1
# Explanation: 3 is not present in array.
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

