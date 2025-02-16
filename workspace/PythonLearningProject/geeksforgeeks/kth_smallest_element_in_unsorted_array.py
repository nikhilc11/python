#######################################################################################################################
# K’th Smallest Element in Unsorted Array
# Last Updated : 14 Aug, 2024
# Given an array arr[] of N distinct elements and a number K, where K is smaller than the size of the array.
# Find the K’th smallest element in the given array.
#
# Examples:
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
# Output: 7
#
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
# Output: 10
#######################################################################################################################

#######################################################################################################################
# Approach - Sort and return value at K-1 index
#######################################################################################################################

def find_kth_smallest_element(arr, k):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    return sorted_arr[k-1]

print(find_kth_smallest_element([7, 10, 4, 3, 20, 15], 3))
print(find_kth_smallest_element([7, 10, 4, 3, 20, 15], 4))

#######################################################################################################################
