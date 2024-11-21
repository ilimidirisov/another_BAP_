#Write a Python function that calculates the product of all elements in an array.
#Example
#Input: [2, 3, 4]
#Output: 24
nums = [2,3,4]
def all_product(nums):
    for i in range(nums):
        nums *= i 
    return nums