class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret = ret + str(len(i)) + "#" + i
        return ret
        
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            # find the next '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            ret.append(word)
            i = j + 1 + length
        return ret
                

            