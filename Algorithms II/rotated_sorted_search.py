#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
        def search(self, nums: List[int], target: int) -> int:
            low = 0
            high = len(nums)-1        
            while low <= high:
                middle = low+(high-low+1)//2
                if nums[middle] == target:
                    return middle
                elif nums[middle] >= nums[low]:
                    if target >= nums[low] and target < nums[middle]:
                        high = middle-1
                    else:
                        low = middle + 1
                else:
                    if target <= nums[high] and target > nums[middle]:
                        low = middle + 1
                    else:
                        high = middle-1


            return -1
        