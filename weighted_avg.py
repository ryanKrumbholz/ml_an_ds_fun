import math

def ascending_weighted_avg(nums):
    n = len(nums)
    min_weight = (1 / n) + 0.01
    weight = min_weight
    total_percent = 0
    avg = 0

    for i in range(n):
        avg += weight * nums[i]
        total_percent += weight
        weight =  1 / (n - i)
    return avg / total_percent

def descending_weighted_avg(nums):
    n = len(nums)
    min_weight = (1 / n) + 0.01
    weight = min_weight
    total_percent = 0
    avg = 0

    for i in range(n - 1, -1, -1):
        avg += weight * nums[n - i - 1]
        total_percent += weight
        print(avg / total_percent)
        weight = 1 / (n - i)
    return avg / total_percent

def avg(nums):
    return sum(nums) / len(nums)



lst = [x for x in range(1,100)]

print(descending_weighted_avg(lst))
print(ascending_weighted_avg(lst))
print(avg(lst))