class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        m=0
        if(len(s)<=1):
            return len(s)
        tmp=set()
        while r<len(s):
            if s[r] not in tmp:
                tmp.add(s[r])
                m=max(m,len(tmp))
                r+=1
            else:
                tmp.remove(s[l])
                l+=1
                
        m=max(m,len(tmp))
        return m