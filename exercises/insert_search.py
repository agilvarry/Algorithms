#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1 
        while low < high:
            middle = low+(high-low+1)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target :
                 high = middle-1
            else:
                low = middle
        if nums[low]==target:
            return low
        elif nums[low] > target:
            return low-1 if low>0 else 0
        else:
            return low+1