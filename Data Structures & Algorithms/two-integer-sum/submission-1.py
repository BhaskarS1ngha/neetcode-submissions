class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        nums_len = len(nums)
        for i in range(nums_len):
            hmap[nums[i]] = i
        for i in range(nums_len):
            diff = target - nums[i]
            j = hmap.get(diff,None)
            if i==j:
                continue
            if j:
                return [i,j]
            