# 5. Longest Palindromic Substring

class Solution:
    # check if s[start:end + 1] is valid palindrome
    def isvalid(self, s: str, start: int, end: int):
        if start < 0 or end >= len(s):
            return False
        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        rtn = s[0]
        for i in range(len(s)):
            # odd length palindrome
            # --palindrome--s[i]--palindrome--
            side = max(int(len(rtn)/ 2), 0)                    
            while self.isvalid(s, i - side, i + side):
                side += 1
            
            if side * 2 - 1 > len(rtn):
                side -= 1
                rtn = s[i - side:i + side + 1]
            
            # even length palindrome
            # --palindrome--s[i]s[i]--palindrome--
            side -= 1
            while self.isvalid(s, i - side, i + side + 1):
                side += 1
            
            if side * 2 > len(rtn):
                side -= 1
                rtn = s[i - side:i + side + 2]
                
        return rtn
