#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        def find_target(target):
            start = 0
            end = len(nums)-1
            while start < end:
                mid = start + ((end-start+1)//2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid
            return start if nums[start] == target else -1
        
        loc = find_target(target)
        if loc == -1:
            return [-1, -1]
        else:
            low, high = loc,loc
            for i in range(loc,-1, -1):
                if nums[i] < target: break
                else: low = i
            for j in range(loc, len(nums)):
                if nums[j] > target: break
                else: high = j

            return [low, high]
            