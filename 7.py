#Write a Python function that sorts an array without using a built-in sort function.
#Example
#Input: [3, 1, 4, 1, 5]
#Output: [1, 1, 3, 4, 5]
nums = [3, 1, 4, 1, 5]
def sort_nums(nums):
    return list(set(nums))

print(sort_nums(nums))