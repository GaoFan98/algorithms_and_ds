def multiply_others(nums):
    right = [1]

    # calc from right to left
    for i in range(len(nums) - 1, 0, -1):
        right.append(right[-1] * nums[i])
        # [1]*5 -> [1,5]
        # 5*4 -> [1,5,20]
        # 20*3 -> [1,5,20,60]

    right = right[::-1]
    # [60,20,5,1]

    left = 1
    # calc from left to right
    # then we multiple every number in right array to the actual array like:
    # 60 * [1]
    # 20 * [2]
    # 5 * [2*3]
    # 1 * [2*3*4]
    for i in range(len(nums)):
        right[i] = right[i] * left
        left = left * nums[i]
        # 60 = 60 * 1 -> 60
        # 1 = 1 * 2 -> 2

        # 20 = 20 * 2 -> 40
        # 2 = 2 * 3 -> 6

        # 5 = 5 * 6 -> 30
        # 6 = 6 * 4 -> 24

    print(right)


out = multiply_others([2, 3, 4, 5])
print(out)
