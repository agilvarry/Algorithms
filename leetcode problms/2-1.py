#https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        num_list = []
        
        for n in num:
            while num_list and k>0 and num_list[-1] >n:
                k -= 1
                num_list.pop()
            num_list.append(n)
            
            
        while k>0:
            num_list.pop()
            k-=1
            
        while num_list[0] == "0" and len(num_list)>1:
            num_list.pop(0)
            
        return "".join(num_list)