# leetcode: 493
nums = [1,3,2,3,1]

def reversePair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > (2 * nums[j]):
                count += 1

    return count


print(reversePair(nums))
