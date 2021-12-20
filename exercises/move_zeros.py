#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        t = 0
        temp = [0] * len(nums)
        while n < len(nums):
            if nums[n] != 0:
                temp[t] = nums[n]
                t+=1
            n+=1
        nums[:] = temp