# Day 2 - Two Sum Problem (HashMap Approach)

# Problem:
# Given an array of integers nums and a target,
# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        dictionary = {}
        
        for i, num in enumerate(nums):
            need = target - num
            
            if need in dictionary:
                return [dictionary[need], i]
            
            dictionary[num] = i
        
        return []


# Example test
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
