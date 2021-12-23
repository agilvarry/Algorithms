#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        
        for i in s:
            if i == '(':
                p.append(i)
            elif i == ')' and len(p)>0 and p[-1] == '(':
                p.pop()
            elif i =='{':
                p.append(i)
            elif i == '}' and len(p)>0 and p[-1] == '{':
                p.pop()
            elif i == '[':
                p.append(i)
            elif i == ']' and len(p)>0 and p[-1] == '[':
                p.pop()
            else:
                return False
            
        return len(p) == 0
        