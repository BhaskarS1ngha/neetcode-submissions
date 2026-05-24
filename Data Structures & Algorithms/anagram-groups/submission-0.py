class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(x)) for x in strs]
        hmap = {x:[] for x in sorted_strs}
        for i in range(len(sorted_strs)):
            hmap[sorted_strs[i]].append(strs[i])
        
        return [x[1] for x in hmap.items()]
