#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return [seen[m], i]
            else:
                seen[n] = i
#https://leetcode.com/problems/3sum/

#https://leetcode.com/problems/4sum/
#https://leetcode.com/problems/4sum/discuss/737096/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation

