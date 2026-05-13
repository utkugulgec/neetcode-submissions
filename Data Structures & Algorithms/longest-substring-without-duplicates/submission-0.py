class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        r = 0
        ans = 0
        for l in range(len(s)):
            a = []
            r=l
            while r<len(s) and s[r] not in a:
                a.append(s[r])
                if ans < len(a):
                    ans=len(a)
                r+=1
        return ans