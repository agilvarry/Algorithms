class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            a=s
            b=t
        else:
            a=t
            b=s
        a_col = collections.Counter(a)
        b_col = collections.Counter(b)

        for val in a_col:
            if val not in b_col or a_col[val] != b_col[val]:
                return False
        return True