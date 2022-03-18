class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def backtrack(permutation, i):
            #if we have reached the length of the word, we're done. append to out
            if i == n:
                out.append(permutation) 
                return
            
            if s[i].isalpha():
                #if the char is a letter swap the case and create a new branch
                backtrack(permutation + s[i].swapcase(), i+1)
            #continue the unswapped branch
            backtrack(permutation + s[i], i+1)
        n = len(s)
        out = []
        backtrack("", 0)
        return out