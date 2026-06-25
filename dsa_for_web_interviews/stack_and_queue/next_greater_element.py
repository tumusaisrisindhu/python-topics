def next_greater(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result


nums = [2, 1, 2, 4, 3]

print(next_greater(nums))