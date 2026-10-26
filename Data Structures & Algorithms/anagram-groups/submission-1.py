class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict={}
        for s in strs:
            key=("").join(sorted(s))
            if not (anag_dict.get(key)):
                anag_dict[key]=[s]
            else:
                tmp=(anag_dict.get(key))
                tmp.append(s)
                anag_dict[key] = tmp

        return (list(anag_dict.values()))
        