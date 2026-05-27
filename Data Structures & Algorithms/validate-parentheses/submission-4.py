class Solution:
    def isValid(self, s: str) -> bool:
        o_brkts = "({["
        c_brkts = {
            ')':'(',
            '}': '{',
            ']': '['
        }
        stk = list()
        for c in s:
            if c in o_brkts:
                stk.append(c)
            else:
                if not stk:
                    return False
                top = stk[-1]
                if c_brkts[c] == top:
                    stk.pop(-1)
                    continue
                else:
                    return False
                
        if stk:
            return False
        return True