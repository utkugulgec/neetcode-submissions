class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        l=0
        r=l+k-1
        d=dict()
        w=dict()

        for c in s1:
            if c not in d:
                d[c]=0
            d[c]+=1
        
        while r<len(s2):
            for c in s2[l:r+1]:
                if c not in w:
                    w[c]=0
                w[c]+=1
            if d == w:
                return True
            l+=1
            r+=1
            w={}
        return False