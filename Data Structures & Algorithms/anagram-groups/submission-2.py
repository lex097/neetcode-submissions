class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        sortedStrs = []
        hashmap = {}
        for i in range(0, len(strs)):
            sortedStrs.append("".join(sorted(strs[i])))
        for i in range(0, len(sortedStrs)):
            if sortedStrs[i] not in hashmap:
                hashmap[sortedStrs[i]] = []
            hashmap[sortedStrs[i]].append(i)
        for key in hashmap:
            addToRet = []
            for index in hashmap[key]:
                addToRet.append(strs[index])
            ret.append(addToRet)
        return ret