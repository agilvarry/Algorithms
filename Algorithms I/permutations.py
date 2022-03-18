class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            #if we've gotten to the end of the list return the current permuration
            if first == n:
                out.append(nums[:])
            for i in range(first,n):
                #swap i and first
                nums[first], nums[i] = nums[i], nums[first]
                #bump first an go deeper
                backtrack(first+1)
                #swap i and first back
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        out = []
        out2 = []
        backtrack(0)
        return out