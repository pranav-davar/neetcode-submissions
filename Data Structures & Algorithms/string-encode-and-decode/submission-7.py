class Solution:
    delimeter='#23'
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return self.delimeter
        return self.delimeter.join(strs)
    def decode(self, s: str) -> List[str]:
        if s is self.delimeter:
            return []
        return s.split(self.delimeter)