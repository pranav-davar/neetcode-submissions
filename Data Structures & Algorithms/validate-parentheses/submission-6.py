class Solution:
    def isValid(self, s: str) -> bool:
        
        r=len(s)
        d={
            '[':']',
            '(':')',
            '{':'}'
        }
        tmp=[]
        for i in range(r):
            if s[i] in set(d.keys()):
                tmp.append(d[s[i]])
                print(s[i])
            else:
                print(s[i])
                if len(tmp)>0 and s[i]==tmp[-1]:
                    tmp.pop()
                else:
                    return False
        if tmp:
            return False
        else:
            return True