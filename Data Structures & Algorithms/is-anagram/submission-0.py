class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        d_s = {x:0 for x in s}
        if d_s.keys() != set(t):
            return False
        
        for x in s:
            d_s[x] +=1
        for x in t: 
            d_s[x] -=1

        for x in d_s:
            if d_s[x] !=0:
                return False
        return True