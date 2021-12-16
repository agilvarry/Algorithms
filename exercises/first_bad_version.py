#https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        
        while low<high:
            middle = low+((high-low+1)//2)
            print(low, high, middle)
            if not isBadVersion(middle) and isBadVersion(middle+1):
                return middle+1
            elif isBadVersion(middle-1):
                high = middle-1
            else:
                low = middle
                
        return low