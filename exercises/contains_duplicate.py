#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {} #dictionary passes but list doesn't because hack table access is faster than array access?
        for i in nums:
            if i in seen:
                return True
            else:
                seen[i] = 1
        
        return False
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort() #hash table is faster, sorting the array uses less space 
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
            