def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):

        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

nums = [2,7,11,15]

print(two_sum(nums, 9))