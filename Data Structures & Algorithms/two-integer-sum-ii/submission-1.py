class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            diff = target-numbers[i]
            res = self.binSearch(numbers[i:],diff)
            if  res !=-1:
                return [i+1, i+res+1]
        return [-1,-1]

    def binSearch(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = left +(right-left)//2
            if arr[mid]==target:
                return mid
            elif target>arr[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1