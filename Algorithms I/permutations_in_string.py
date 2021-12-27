#https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        c1 = collections.Counter()
        c2 = collections.Counter()
        for w in s1:
            c1[w] += 1
        
        for j in range(len(s2)):
            c2[s2[j]] +=1
            if j >= l:
                if c2[s2[j-l]] ==1:
                    del c2[s2[j-l]]
                else:
                    c2[s2[j-l]]-=1
            if c1==c2:
                return True
        return False