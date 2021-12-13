#https://leetcode.com/problems/counting-bits/
class Solution:
    """
    This should help:
    https://realpython.com/python-bitwise-operators/
    """   
    def countBits(self, n: int) -> List[int]:
                 
        ones = []
        for i in range(n+1):
            count = self.count_ones(i)
            ones.append(count)  
        return ones
    
    def count_ones(self, n) -> int:
        """
        here we drop bits from the input number, and use a bitwise and to see if the right most
        bit is a 1, incrementing count as we go
        """
        count = 0
        while n:
            count +=  n & 1 #bitwise AND only returns a 1 when there is a 1 in the right most binary representation of n
            n >>= 1 #we're dropping the right most bit off the number here
        return count 
        