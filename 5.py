#Write a Python function that removes duplicate elements from an array.
#Example
#Input: [1, 2, 2, 3, 3, 4]
#Output: [1, 2, 3, 4]
nums = [1, 2, 2, 3, 3, 4]
def remove_duplicates(nums):
    return list(set(nums))

result = remove_duplicates(nums)
print (result)