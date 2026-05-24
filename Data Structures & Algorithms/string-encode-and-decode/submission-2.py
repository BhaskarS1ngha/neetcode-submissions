class Solution:

    def encode(self, strs):
        str_lens = [len(s) for s in strs]
        encoded_strs = f"{str_lens};{''.join(strs)}"
        return encoded_strs

    def decode(self, s: str):
        idx_map = s[:s.index(';')]
        s = s[s.index(';')+1:]
        print(idx_map)
        if len(idx_map)==2:
            return []
        idxs = [int(x)  for x in idx_map[1:-1].split(',')]
        strs = list()
        prev=0
        for i in idxs:
            t = s[prev:prev+i]

            strs.append(t)
            prev+=i
        return strs