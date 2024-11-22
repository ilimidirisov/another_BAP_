#Write a Python function that checks if an array has duplicate elements and prints "Yes" or "No".
#Example
#Input: [1, 2, 3, 1]
#Output: Yes
nums = [1, 2, 3, 1]
def duplicate_founder(nums):
    return list(set(nums))