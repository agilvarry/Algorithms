class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        #if beg of list is less than end list is unrotated
        if nums[0] < nums[high] or len(nums)==1:
            return nums[0]
        
        
        while low <= high:
            mid = low + (high-low) // 2
            #if middle element is greater than next right, next right is lowest
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            #if next left is greater than mid then mid is lowest
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            #if lowest is less than mid, new low is right of mid
            if nums[mid] > nums[0]:
                low = mid + 1
            #else new high is left of mid
            else:
                high = mid-1