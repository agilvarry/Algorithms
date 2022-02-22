#https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        bits = 0
        for i in range(32):
            if n & mask !=0:
                bits += 1
            mask = mask << 1
            
        return bits