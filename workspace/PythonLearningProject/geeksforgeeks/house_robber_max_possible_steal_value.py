#######################################################################################################################
#
# There are n houses built in a line, each of which contains some money in it.
# A robber wants to steal money from these houses, but he can’t steal from two adjacent houses.
# The task is to find the maximum amount of money which can be stolen.
#
# Examples:
#
# Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
# Output: 19
# Explanation: The thief will steal from house 1, 3, 5 and 7, total money = 6 + 1 + 8 + 4 = 19.
#
# Input: hval[] = {5, 3, 4, 11, 2}
# Output: 16
# Explanation: Thief will steal from house 1 and 4, total money = 5 + 11 = 16.
#
#######################################################################################################################

#######################################################################################################################
# Solution 1 - Recursion Approach - Naive Approach
#######################################################################################################################

print("Solution 1 - Recursion Approach")


def max_loot_record(house_values_list, house_count):
    if house_count == 0:
        return 0

    if house_count == 1:
        return house_values_list[0]

    set_1_val = house_values_list[house_count - 1] + max_loot_record(house_values_list, house_count - 2)

    set_2_val = max_loot_record(house_values_list, house_count - 1)

    return max(set_2_val, set_1_val)


def max_loot(house_values_list):
    house_count = len(house_values_list)
    return max_loot_record(house_values_list, house_count)


print(max_loot([6, 7, 1, 3, 8, 2, 4]))

print(max_loot([5, 3, 4, 11, 2]))

#######################################################################################################################
# Solution 2 - Memoization - Top Down Approach
#######################################################################################################################

print("Solution 2 - Memoization Approach - Top Down Approach")


def max_loot_record_v2(house_values_list, house_count, house_memo):
    if house_count <= 0:
        return 0
    if house_count == 1:
        return house_values_list[0]

    if house_memo[house_count] != -1:
        return house_memo[house_count]

    set_1_val = house_values_list[house_count - 1] + max_loot_record_v2(house_values_list, house_count - 2, house_memo)

    set_2_val = max_loot_record_v2(house_values_list, house_count - 1, house_memo)

    house_memo[house_count] = max(set_1_val, set_2_val)

    return house_memo[house_count]


def max_loot_v2(house_values_list):
    house_count = len(house_values_list)
    house_memo = [-1] * (house_count + 1)
    return max_loot_record_v2(house_values_list, house_count, house_memo)


print(max_loot_v2([6, 7, 1, 3, 8, 2, 4]))

print(max_loot_v2([5, 3, 4, 11, 2]))

#######################################################################################################################
# Solution 3 - Tabulation - Dynamic Programming - Bottom Up Approach
#######################################################################################################################

print("Solution 3 - Tabulation - Dynamic Programming - Bottom Up Approach")


def max_loot_v3(house_values_list):
    house_count = len(house_values_list)

    dp = [0] * (house_count + 1)

    dp[0] = 0
    dp[1] = house_values_list[0]

    for i in range(2, house_count + 1):
        dp[i] = max(house_values_list[i - 1] + dp[i - 2], dp[i - 1])

    return dp[house_count]


# hv = [   5,       3,       4,        11,         2]
# dp = [0, 5, 3+0/5=5, 4+5/5=9, 11+5/9=16, 2+9/16=16]

# hv = [   6,       7,         1,        3,         8,          2,          4]
# dp = [0, 6, 7+0/6=7, 1+6/7 = 7, 3+7/7=10, 8+7/10=15, 2+10/15=15, 4+15/15=19]

print(max_loot_v3([6, 7, 1, 3, 8, 2, 4]))
print(max_loot_v3([5, 3, 4, 11, 2]))

#######################################################################################################################
# Solution 4 - Tabulation - Space Optimized - Dynamic Programming - Bottom Up Approach
#######################################################################################################################

print("Solution 4 - Tabulation - Space Optimized - Dynamic Programming - Bottom Up Approach")


def max_loot_v4(house_values_list):
    house_count = len(house_values_list)

    dp_2 = 0
    dp_1 = house_values_list[0]

    for i in range(2, house_count + 1):
        dp = max(house_values_list[i - 1] + dp_2, dp_1)
        dp_2 = dp_1
        dp_1 = dp

    return dp


print(max_loot_v4([6, 7, 1, 3, 8, 2, 4]))
print(max_loot_v4([5, 3, 4, 11, 2]))

#######################################################################################################################
