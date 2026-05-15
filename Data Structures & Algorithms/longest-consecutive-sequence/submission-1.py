class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        l = 0
        for i in nums:
            s.add(i)

        for i in s:
            if i-1 not in s:
                k=0
                while i+k in s:
                    k+=1
                l=max(l,k)
        return l