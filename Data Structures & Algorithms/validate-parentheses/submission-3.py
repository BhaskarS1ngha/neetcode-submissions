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
                try:
                    top = stk[-1]
                    if c_brkts[c] == top:
                        stk.pop(-1)
                        continue
                    else:
                        return False
                except IndexError as e:
                    return False
        if stk:
            return False
        return True