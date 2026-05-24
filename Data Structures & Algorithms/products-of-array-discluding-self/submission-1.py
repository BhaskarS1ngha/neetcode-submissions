class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prod = 1
        for i in nums:
            if i !=0:
                prod*=i
            else:
                if zero_cnt!=0:
                    return [0]* len(nums)
                else:
                    zero_cnt +=1
        res = []
        if zero_cnt != 0:
            for i in nums:
                if i ==0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        else:
            return [prod//i for i in nums]