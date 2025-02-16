#######################################################################################################################
#
# Largest sum subarray
#
# Given an array of integers, find the contiguous subarray (containing at least one element)
# that has the largest sum and return the sum.
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#######################################################################################################################

#######################################################################################################################
# Approach - Kadane's Algorithm
#######################################################################################################################

def findLargestSumSubArray(array):

    print(f"Input Array = {array}")

    result = 0
    max_ending_sum = 0
    subarray_starting_position = 0
    subarray_ending_position = 0

    for i in range(0, len(array)):

        if max_ending_sum + array[i] > arr[i]:
            max_ending_sum += array[i]

        else:
            max_ending_sum = array[i]
            subarray_starting_position = i
            subarray_ending_position = i

        if max_ending_sum >= result:
            result = max_ending_sum
            subarray_ending_position = i

        print(f"index = {i}, \t"
              f"element = {array[i]}, \t"
              f"max_ending_sum = {max_ending_sum}, \t"
              f"result = {result}, \t"
              f"subarray_starting_position = {subarray_starting_position}, \t"
              f"subarray_ending_position = {subarray_ending_position}. \t")

    return (result,
            subarray_starting_position,
            subarray_ending_position,
            array[slice(subarray_starting_position, subarray_ending_position+1)])


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sum_value, st_index, end_index, sub_array = findLargestSumSubArray(arr)

print(f"Array = {arr}")
print(f"Sum = {sum_value}")
print(f"Sub Array Starting Index is {st_index}")
print(f"Sub Array Ending   Index is {end_index}")
print(f"Sub Array Elements are {sub_array}")

#######################################################################################################################
