#Name: Andrew Lee
#OSU CS 325
#Assignment 4, Problem 1
#Due Date: January 5, 2023

def max_independent_set(nums):
    condition = False
    for x in nums:
        if x >= 0:
            condition = True
    if condition == False:
        return []
    table = []
    number_used = []
    for x in range(len(nums)):
        table.append(nums[x])
        number_used.append(x)
    for x in range(len(nums)):
        if (x+2) > len(nums)-1:
            pass
        else:
            for y in range((x+2), len(nums)):
                temporary_result = table[x] + nums[y]
                if temporary_result > table[y]:
                    table[y] = temporary_result
                    number_used[y] = x
    result = 0
    for m in range(len(table)):
        if table[m] > result:
            result = m
    actual_result = []
    while result >= 0:
        if result == 0:
            actual_result.insert(0, nums[result])
            result = -1
        else:
            actual_result.insert(0, nums[result])
            result = number_used[result]
    return actual_result

