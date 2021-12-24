#https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        
        for i in range(len(s)):
            c = s[i]
            if c in seen:
                seen[c]['count'] += 1
            else:
                seen[c] = {'count': 1, 'idx': i }
                

        
        for val in seen:
            if seen[val]['count'] == 1:
                return seen[val]['idx']
            
        return -1