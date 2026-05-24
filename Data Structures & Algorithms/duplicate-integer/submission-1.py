class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {x:0 for x in nums}
        for n in nums:
            nums_dict[n] += 1
            if nums_dict[n] >1:
                return True
        return False
            