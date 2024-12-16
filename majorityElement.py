# This is None brute force approach (that ive came up with on my own)
# 1. time complexity of this is O(nlogn)
# def majaorityElement(nums):
#     nums.sort()
#     count = 1
#     n = len(nums)
#     for i in range(1, n):
#         if nums[i] == nums[i - 1]:
#             count += 1
#         else:
#             count = 1

#         if count > (n // 2):
#             return nums[i]
#     return nums[0]
# majority = majaorityElement(nums)

# 2. Dictionary approach
# from collections import defaultdict

# def majaorityElement(nums):
#     freq_count = defaultdict(int)

#     # counting the appearances of each element
#     for num in nums:
#         freq_count[num] += 1
#         # Checking in the dictionary for the frequency greator than half of the length of the list
#         if freq_count[num] > len(nums) // 2:
#             return num
#     return None

# 3. very smart approach
# def majaorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]

# 4. Moore's algorithm
# def majorityElement(nums):
#     count = 0
#     for i in range(len(nums)):
#         if count == 0:
#             el = nums[i]
#             count = 1
#         elif nums[i] == el:
#             count += 1
#         else:
#             count -= 1
#     return el


def majorityElement(nums):
    nums.sort()
    print(nums)
    goal = len(nums) / 2
    count = 0
    maxCount = 0
    mostInt = 0

    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count
            mostInt = nums[i]
    return mostInt


nums = [2, 2, 1, 1, 1]
print(majorityElement(nums))
