#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        cpy1 = nums1[:m]
        for k in range(n+m):
            if j >= n or (i<m and cpy1[i] <= nums2[j]):
                nums1[k] = cpy1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j+=1
      