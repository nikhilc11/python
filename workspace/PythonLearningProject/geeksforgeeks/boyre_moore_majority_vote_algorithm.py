nums = [2, 1, 2, 2, 2, 1, 1, 3, 2]

def majorityElement(arr):
    candidate, count = 0,0

    for i in range(len(arr)):
        if count == 0:
            candidate = arr[i]
            if arr[i] == candidate:
                count += 1
            else:
                count -= 1

    return candidate


print(majorityElement(nums))