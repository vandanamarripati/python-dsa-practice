# Day 2 - Contains Duplicate

# Problem:
# Given an array of integers, return True if any value appears at least twice.

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


# Test cases
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4]))      # False
print(sol.containsDuplicate([1, 2, 3, 1]))      # True
print(sol.containsDuplicate([5, 5, 5, 5]))      # True
