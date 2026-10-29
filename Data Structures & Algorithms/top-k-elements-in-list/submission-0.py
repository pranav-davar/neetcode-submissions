class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ledger={}
        for i in nums:
            ledger[i]=ledger.get(i,0) + 1
        out=[]
        for i in range(k):
            tmp=(max(ledger,key=ledger.get))
            out.append(tmp)
            ledger.pop(tmp)
        return out