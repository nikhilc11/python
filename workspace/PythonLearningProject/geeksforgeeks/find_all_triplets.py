#######################################################################################################################
# Given an array arr[], the task is to find all possible indices {i, j, k} of triplet
# {arr[i], arr[j], arr[k]} such that their sum is equal to zero and all indices in a triplet
# should be distinct (i != j, j != k, k != i).
# We need to return indices of a triplet in sorted order, i.e., i < j < k.
#######################################################################################################################
#
# input
# [0, -1, 2, -3, 1]
#
# expected output
# [[0, 1, 4], [2, 3, 4]]
#
#######################################################################################################################
# Method 1 - Complexity
# Time -> O(n^3)
# Space -> O(n)
#######################################################################################################################

print("Solution 1")

def find_triplets_sum_to_zero(array_list):
    output_list = []
    array_length = len(array_list)
    for i in range(0, array_length - 2):
        for j in range(i + 1, array_length - 1):
            for k in range(j + 1, array_length):
                if array_list[i] + array_list[j] + array_list[k] == 0:
                    output_list.append([i, j, k])
    return output_list


{print(triplets) for triplets in find_triplets_sum_to_zero([0, -1, 2, -3, 1])}

#######################################################################################################################
# Given an array arr[], and an integer target, find all possible unique triplets in the array whose sum is equal to the
# given target value. We can return triplets in any order, but all the returned triplets should be internally sorted,
# i.e., for any triplet [q1, q2, q3], the condition q1 ≤ q2 ≤ q3 should hold.
#######################################################################################################################
# Method 2 - Complexity
# Time -> O(n^2)
# Space -> O(n)
#######################################################################################################################

print("Solution 2")

def find_triplets_with_sum(array_list, sum_target):
    output_list = []
    pos_output_list = []
    array_length = len(array_list)

    for i in range(0,array_length-2):
        prev_j_val_to_pos_dict = {}
        current_target = sum_target - array_list[i]

        for j in range(i+1, array_length):
            j_diff = current_target - array_list[j]
            if j_diff in prev_j_val_to_pos_dict:
                output_list.append(sorted([array_list[i], j_diff, array_list[j]]))
                pos_output_list.append(sorted([i, prev_j_val_to_pos_dict[j_diff], j]))
            prev_j_val_to_pos_dict[array_list[j]] = j
    # return pos_output_list
    return output_list


{print(triplets) for triplets in find_triplets_with_sum([12, 3, 6, 1, 6, 9], 24)}


#######################################################################################################################
# Given three sorted arrays A[], B[] and C[],
# find 3 elements i, j and k from A, B and C respectively such that
# max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized.
# Here abs() indicates absolute value.
#######################################################################################################################

print("Solution 3")

def identify_minimum_difference():
    A = [1, 4, 10]
    B = [2, 15, 20]
    C = [10, 12]

    min_val = float('inf')
    result_list = []

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(C)):
                if max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) < min_val:
                    min_val = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
                    result_list = [A[i],B[j],C[k]]

    print(result_list)

identify_minimum_difference()

#######################################################################################################################
# Given an array of positive integers, the task is to determine if a Pythagorean triplet exists in the given array.
# A triplet {a, b, c} is considered a Pythagorean triplet if it satisfies the condition a2 + b2 = c2.
#######################################################################################################################

print("Solution 4")

def identify_pythagorean_set_exists(arr):

    arr.sort()

    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if arr[i]**2 + arr[j]**2 == arr[k]**2:
                    print([arr[i],arr[j],arr[k]])
                    return True
    return False


print(identify_pythagorean_set_exists([3, 1, 4, 6, 5]))
print(identify_pythagorean_set_exists([10, 4, 6, 12, 5]))

#######################################################################################################################
# Given a positive integer target, the task is to find all Pythagorean Triplets whose sum of the elements is equal to
# the given target. A triplet {a, b, c} is considered a Pythagorean triplet if it satisfies the condition a2 + b2 = c2.
#######################################################################################################################

print("Solution 5")

def identify_pythagorean_set_for_target_sum(target):

    for a in range(1,target-2):
        for b in range(a+1,target-1):
            c = target - a - b
            if c <= b :
                continue
            if a**2 + b**2 == c**2:
                print([a, b, c])

identify_pythagorean_set_for_target_sum(60)

#######################################################################################################################
# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value.
# The expected Time Complexity is O(n2).
#######################################################################################################################

print("Solution 6")

def identify_triplets_with_sum_lesser_than_target(arr, target_sum):
    count = 0
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] < target_sum:
                    count += 1
    return count

print(identify_triplets_with_sum_lesser_than_target([-2, 0, 1, 3], 2))
print(identify_triplets_with_sum_lesser_than_target([5, 1, 3, 4, 7], 12))

def identify_triplets_with_sum_lesser_than_target_v2(arr, target_sum):
    count = 0
    for i in range(0, len(arr)-2):
        j = i+1
        k = len(arr)-1

        while (j<k):
            if arr[i] + arr[j] + arr[k] >= target_sum:
                k-=1
            else:
                count += k-j;
                j+=1
    return count

print(identify_triplets_with_sum_lesser_than_target_v2([-2, 0, 1, 3], 2))
print(identify_triplets_with_sum_lesser_than_target_v2([5, 1, 3, 4, 7], 12))

#######################################################################################################################
