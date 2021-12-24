#https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            j=list(words[i])
            j = self.reverseString(j)
            words[i] = "".join(j)
        return " ".join(words)
        
        
    def reverseString(self, s: List[str]) -> None:
        low = 0
        high = len(s)-1        
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return s