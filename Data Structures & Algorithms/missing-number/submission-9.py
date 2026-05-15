class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        for i in range(len(nums)+1):
            if i>=len(nums) or i != nums[i]:
                return i