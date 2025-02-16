#######################################################################################################################
#
# Given a binary 2D array, where each row is sorted. Find the row with the maximum number of 1s.
#
# Examples:
#
# Input matrix : 0 1 1 1
#                0 0 1 1
#                1 1 1 1
#                0 0 0 0
# Output: 2
# Explanation: Row = 2 has maximum number of 1s, that is 4.
#
#
# Input matrix : 0 0 1 1
#                0 1 1 1
#                0 0 1 1
#                0 0 0 0
# Output: 1
# Explanation: Row = 1 has maximum number of 1s, that is 3.
#######################################################################################################################

#######################################################################################################################
# Approach - Sum each row and return row with max sum
#######################################################################################################################

def row_with_max_ones(mat):
    index = 0
    max_ones_count = 0
    max_ones_line = 0
    for line in mat:
        print(line)
        line_sum = sum(line)
        if line_sum > max_ones_count:
            max_ones_count = line_sum
            max_ones_line = index
        index += 1
    return max_ones_line


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print("Index of row with maximum 1s is " + str(row_with_max_ones(mat)))

#######################################################################################################################
