#https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def robFrom(i, nums):
            
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
                        #rob the next one    #rob this skip next
                
            cash = max(robFrom(i + 1, nums), robFrom(i + 2, nums) + nums[i])
            
            #save
            memo[i] = cash
            return cash
        
        memo = {}
        
        return robFrom(0, nums)