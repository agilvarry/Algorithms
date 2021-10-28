#https://leetcode.com/problems/wiggle-sort-ii/
#basically fast but not very memory efficient
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = len(nums)
        m = l // 2
        if l%2 == 1:
            m+=1
        
        
        small = nums[:m]
        large = nums[m:]
        
        for i in range(0, len(nums)):
            if i %2==0:
                nums[i] = small.pop(-1)
            else:
                nums[i] = large.pop(-1)