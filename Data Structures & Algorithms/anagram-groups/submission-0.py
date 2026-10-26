class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict={}
        for s in strs:
            
            if not (anag_dict.get(("").join(sorted(s)))):
                anag_dict[("").join(sorted(s))]=[s]
            else:
                tmp=((anag_dict.get(("").join(sorted(s)))))
                tmp.append(s)
                anag_dict[("").join(sorted(s))] = tmp

        return (list(anag_dict.values()))
        