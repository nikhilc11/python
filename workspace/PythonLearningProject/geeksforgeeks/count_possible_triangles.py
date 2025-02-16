#######################################################################################################################
# Given an unsorted array of positive integers, the task is to find the number of triangles that can be formed with
# three different array elements as three sides of triangles.
#
# For a triangle to be possible from 3 values as sides, the sum of the two values (or sides) must always be greater
# than the third value (or third side).
#
# Examples:
#
# Input: arr[] = [4, 6, 3, 7]
# Output: 3
# Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7].
# Note that [3, 4, 7] is not a possible triangle.
#
#
# Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
# Output: 6
# Explanation: There can be 6 possible triangles:
# [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]
#
#
# Input: arr[] = [1, 2, 3]
# Output: 0
# Examples: No triangles are possible.
#######################################################################################################################

#######################################################################################################################
# Solution 1
#######################################################################################################################

def find_possible_triangles(arr):
    print("Find Triangles")
    print(arr)
    arr.sort()
    print(arr)
    triangles_set = set()

    for i in range(0,len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j]) > arr[k]:
                    tri_element = str([arr[i], arr[j], arr[k]])
                    triangles_set.add(tri_element)
    return triangles_set


array_list = [4, 6, 3, 7]

tri_set = find_possible_triangles(array_list)

print("Triangles")
{print(tri) for tri in tri_set}

#######################################################################################################################
# Solution 2
# Space O(n^2)
# Time O(1)
#######################################################################################################################

def count_triangles(arr):
    print("Find Triangles v2")
    print(arr)
    arr.sort()
    print(arr)
    triangles_count = 0

    for i in range(2,len(arr)):
        left = 0
        right = i-1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                triangles_count += right - left
                right -= 1
            else:
                left += 1
    return triangles_count


# 4,6,3,7
# 3,4,6,7
# FOR -> i=2
# FOR -> i=2 -> While -> l=0 -> r=1 -> IF -> 3+4>6 -> (r-l)=1 -> s=1 -> r=0
# FOR -> i=2 -> While -> l=0 -> r=0 -> Exit While
# FOR -> i=3 -> While -> l=0 -> r=2 -> IF -> 3+6>7 -> (r-l)=2 -> s=3 -> r=1
# FOR -> i=3 -> While -> l=0 -> r=1 -> IF -> 3+4>7 -> l=1
# FOR -> i=3 -> While -> l=1 -> r=1 -> Exit While
# FOR -> i=3 -> Exit For
# s = 3

print(f"Triangles Count: {count_triangles([4, 6, 3, 7])}")

print(f"Triangles Count: {count_triangles([10, 21, 22, 100, 101, 200, 300])}")

# [10, 21, 22, 100, 101, 200, 300]
# [ 10,  21,  22]  1
# [ 10,  22, 100]  0
# [ 21,  22, 100]  0
# [ 10, 100, 101]  3
# [ 10,  22, 101]  0
# [ 21,  22, 101]  0
# [ 10, 101, 200]  0
# [ 21, 101, 200]  0
# [ 22, 101, 200]  0
# [100, 101, 200]  1
# [ 10, 200, 300]  0
# [ 21, 200, 300]  0
# [ 22, 200, 300]  0
# [100, 200, 300]  0
# [101, 200, 300]  1

#######################################################################################################################
