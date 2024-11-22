#Write a Python function that finds the sum of elements at even indices in an array.
#Example
#Input: [1, 2, 3, 4, 5]
#Output: 9
nums = [1, 2, 3, 4, 5]

def sum_of_indices(nums):
    total = 0 
    for i in range (len(nums)):
        if nums[i] % 2 == 1:
            total += i        
    return total
print(sum_of_indices(nums))