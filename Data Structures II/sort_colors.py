#https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        two = len(nums)-1
        zero = 0
        i = 0
        
        while i <= two:
            if nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            elif nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i +=1
            else:
                i +=1
        return nums
        