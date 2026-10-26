class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out=[]
        s=None
        for i in range(len(nums)):
            if (target-nums[i] in set(nums[i+1::]) and s is None):
                out.append(i)
                s=target-nums[i]
            if (s==nums[i] and out[0]!=i):
                out.append(i)
                return out
