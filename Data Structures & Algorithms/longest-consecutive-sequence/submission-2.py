class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        hmap = {x:True for x in nums}
        max = 1

        for x in nums:
            y = x-1
            if not hmap.get(y,False):
                continue
            count = 1
            z=y
            while True:
                z+=1
                if not hmap.get(z,False):
                    break
                count +=1

            if max<count:
                max = count
        return max
