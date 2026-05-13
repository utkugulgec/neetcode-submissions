class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        h = 1
        t = 1
        ha = []
        ta = []
        for i in range(len(nums)):
            if i == 0:
                ha.append(h)
                continue
            h=h*nums[i-1]
            ha.append(h)
        nums.reverse()
        for i in range(len(nums)):
            if i == 0:
                ta.append(t)
                continue
            t=t*nums[i-1]
            ta.append(t)
        print(ta)    
        ta.reverse()
        return [a * b for a, b in zip(ha,ta)]
