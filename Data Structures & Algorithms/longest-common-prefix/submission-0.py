class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        i=0
        if len(first) <= len(last):
            lim=len(first)
        else:
            lim=len(last)
        ans=0
        for idx in range(lim):
            if first[idx]==last[idx]:
                ans+=1
            else:
                break
        return first[0:ans]    