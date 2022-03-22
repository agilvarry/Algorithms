#https://leetcode.com/problems/3sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        #similar to original twoSum, but we collect all sums that equal target, not the idx
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                res.append([m, n])
            else:
                seen[n] = i
        return res
                
                
                
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: #this checks if the value is the same as the previous in the sorted list
                continue
            o = self.twoSum(nums[i+1:],-nums[i]) #target is negative of current num, so if we reach 0 in 2sum that's an answer
            if o ==[]:
                continue
            else:
                for idx in o:
                    idx.append(nums[i])
                    res.append(idx)
        out = []  
        #filter out any duplicate lists
        for idx in res: 
            if idx not in out:
                out.append(idx)
        return out
            