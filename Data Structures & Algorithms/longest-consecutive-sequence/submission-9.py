class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss= set(nums)
        if(len(nums)==0):
            return 0
        # seq= {}
        max_len=0
        print(numss)
        for i in numss:
            if i - 1 not in numss:
                curr = i
                curr_len = 1
                while curr + 1 in numss:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len