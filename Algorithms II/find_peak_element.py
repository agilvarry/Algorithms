class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def recurse(low, high):
            print(low, high)
            if high == low:
                return high            
            mid = low + (high-low) // 2
            if nums[mid] > nums[mid+1]:
                return recurse(low, mid)
            return recurse(mid+1, high)
        
        return recurse(0, len(nums)-1)
        