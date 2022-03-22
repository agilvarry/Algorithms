#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #this is so simple to do using a dictionary in python
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
        #O(1) space complexity solution
        #Boyer-Moore Voting Algorithm
#         count = 0
#         candidate = None
        
#         for num in nums:
            
#             if count == 0:
#                 candidate = num
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1
            
#         return candidate
        
        