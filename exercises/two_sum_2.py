#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            m = target-n
            if m in seen:
                return[seen[m],i+1]
            else:
                seen[n] = i+1