#https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)
        
        for val in ransom_count:
            if val not in mag_count or ransom_count[val] > mag_count[val]:
                return False
        
        return True