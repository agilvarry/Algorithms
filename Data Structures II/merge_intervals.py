#https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        #sort on i[0]
        intervals.sort(key= lambda i: i[0])
        for i in intervals:
            if len(out) == 0 or out[-1][1] < i[0]:
                out.append(i)
            else:
                out[-1][1] = max(out[-1][1], i[1])
        return out
                