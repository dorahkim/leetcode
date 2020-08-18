# 6. ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #corner case
        if numRows == 0 or len(s) == 0:
            return ""
        #simple case
        elif numRows == 1:
            return s
        elif numRows >= len(s):
            return s
        
        #generate strings for each row
        strs = ['' for i in range(numRows)]
        
        #True: 0, 1, 2, ...
        #False: numRows - 1, numRows - 2, ...
        increase = True
        row = 0
        
        for i in range(len(s)):
            strs[row] += s[i]
            if increase:
                if row == numRows - 1:
                    row -= 1
                    increase = False
                else:
                    row += 1
            else:
                if row == 0:
                    row += 1
                    increase = True
                else:
                    row -= 1
        
        return ''.join(strs)
