#Write a Python function that calculates the product of all elements in an array.
#Example
#Input: [2, 3, 4]
#Output: 24
nums = [2,3,4]
def product_of_nums(nums): 
    total = 1     
    for i in range(len(nums)):
        total *= i 
    return total 
print(nums)
