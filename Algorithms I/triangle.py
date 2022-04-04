#https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:   
        @lru_cache(maxsize=None)
        def helper(t, loc):
            res = triangle[t][loc]
            if len(triangle)-1 <= t:
                return res
            else:
                res += min(helper(t+1, loc), helper(t+1, loc+1))
                return res
        return helper(0,0)