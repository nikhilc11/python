print("Solution 1:")

def segregate_digits(arr, distinct_digits):
    cnt_arr = [0]*distinct_digits
    for i in range(len(arr)):
        cnt_arr[arr[i]] += 1

    result_list = list()
    for i in range(distinct_digits):
        result_list += [i] * cnt_arr[i]

    return result_list


arr = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
print(arr)
print(segregate_digits(arr, 3))

arr = [0, 1, 2, 0, 1, 2]
print(arr)
print(segregate_digits(arr, 3))

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(arr)
print(segregate_digits(arr, 3))



print("Solution 2:")

def segregate_digits_v2(arr):
    low = 0
    high = len(arr)-1

    while low < high :
        if arr[low] == 1 and arr[high] == 0:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        elif arr[low] == 1 and arr[high] == 1:
            high -= 1
        else:
            low += 1

arr = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
print(arr)
segregate_digits_v2(arr)
print(arr)
