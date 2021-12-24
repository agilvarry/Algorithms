#https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1        
        while low < high:
            middle = low+((high-low+1)//2)
            print(middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target :
                 high = middle-1
            else:
                low = middle

        return low if nums[low]==target else -1