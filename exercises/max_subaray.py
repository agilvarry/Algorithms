#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #this starts by setting the current and best sum to the first item in the array
        best_sum = nums[0]
        current_sum = nums[0]
        for n in nums[1:]:
            """
            this loops starts at item 2 and keeps a sum. 
            Any time the sum is less than the current item
            we know we can ignore items that came previously.
            we then see if the current sum is better than our best so far
            """
            current_sum = max(n, current_sum + n)
            best_sum = max(best_sum, current_sum)
        return best_sum