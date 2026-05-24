class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive approach
        res = list()
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j==i:
                    continue
                prod *=nums[j]
            res.append(prod)
        
        return res