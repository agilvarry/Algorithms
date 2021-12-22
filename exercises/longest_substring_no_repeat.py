#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        long=""
        for i in s:
            if i in long:
                long= long.split(i)[1]+i
            else:
                long = long+i
                if len(long)>longest:
                    longest += 1
        return longest