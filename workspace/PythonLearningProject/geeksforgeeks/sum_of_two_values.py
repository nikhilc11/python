#######################################################################################################################
#
# Given an array of integers arr and a target value t,
# find two array indices such that the values stored at those positions add up to t.
# Return these indices, ensuring each index is used only once.
# There is exactly one valid solution.
#
#######################################################################################################################

#######################################################################################################################
# Approach -
#######################################################################################################################

def find_elements_with_sum(array_list, sum_val):
    index_pair_set = set()
    for index in range(len(array_list)):
        try:
            find_index = array_list.index(sum_val - array_list[index])
        except Exception:
            continue
        else:
            if index < find_index:
                index_pair_set.add(str([index, find_index]))
    return index_pair_set


print(find_elements_with_sum([2, 7, 11, 15], 9))
print(find_elements_with_sum([3, 2, 4], 6))
print(find_elements_with_sum([1, 3, 2, 4, 5], 6))

#######################################################################################################################
