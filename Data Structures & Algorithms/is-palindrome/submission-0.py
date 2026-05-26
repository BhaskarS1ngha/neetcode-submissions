import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = re.sub('[^A-Za-z0-9]+','',s).lower()
        filtered_str_len = len(filtered_str)
        midPoint = filtered_str_len//2
        for i in range(0,midPoint):
            if filtered_str[i] != filtered_str[filtered_str_len-1-i]:
                return False
            
        return True