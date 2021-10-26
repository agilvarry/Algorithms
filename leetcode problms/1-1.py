"""Given an array of integers temperatures represents the daily temperatures, return an array answer such 
that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead."""
#https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        memory =[]
        for i, temp in enumerate(temperatures):
            while memory and temp > memory[-1][1]: 
                """
                when the current temp is larger that the most recent item in the stack,
                we calculate the different between the index and that's our day.
                This allows us to progress through the list with the largest temp that hasn't been passed being first.
                This is a monotonic stack solution.
                """
                j, t = memory.pop()
                answer[j] = i-j
                
            memory.append([i, temp]) #add the index and temp to a nested list "stack"
        return answer