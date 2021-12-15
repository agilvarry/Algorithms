#https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []
                    
        for i in nums1:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for j in nums2:
            if j in seen and seen[j] > 0:
                seen[j] -= 1
                res.append(j)
        return res