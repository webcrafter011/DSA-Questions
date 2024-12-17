# def consecutiveSeq(nums):
#     nums.sort()
#     global_count = 0
#     current_count = 1
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1] - 1:
#             current_count += 1
#             if current_count > global_count:
#                 global_count = current_count
#             else:
#                 current_count = 0
#     return global_count


def consecutiveSeq(nums):
    st = set()
    longest = 1

    # populating the set with array values
    for i in range(len(nums)):
        st.add(nums[i])

    # iterate over the set
    for el in st:
        # check if there exist an element which smaller than the current element by one if not then execute this
        if el - 1 not in st:
            count = 1
            x = el
            # a loop to count how many consecutive values exist in the set
            while x + 1 in st:
                x += 1
                count += 1
            longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(consecutiveSeq(nums))
