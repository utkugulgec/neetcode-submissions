class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        l = sorted(d.items(), key=lambda item: item[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(l[i][0])
        return ans