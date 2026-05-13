class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []
        for j, val in enumerate(nums):
            indexed_nums.append((val, j))

        indexed_nums.sort()
        nums = sorted(nums) 

        i = 0
        j = len(nums)-1
        
        while (i<j):
            if (nums[i]+nums[j]) < target:
                i+=1
            elif (nums[i]+nums[j]) > target:
                j-=1
            else:
                res = sorted([indexed_nums[i][1], indexed_nums[j][1]])
                return res