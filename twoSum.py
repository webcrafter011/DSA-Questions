nums = [2, 7, 13, 14, 5, 6, 8]
target = 15

def twoSum(nums, target):
    # Hash map to store the value and its index
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num  # Find the difference needed to reach target
        
        # Check if the complement is already in the map
        if complement in num_map:
            return [i, num_map[complement]]  # Return the indices of the two numbers
        
        # Store the current number and its index in the map
        num_map[num] = i

# Function call and print the result
result = twoSum(nums, target)
print(result)
