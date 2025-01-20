class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        result = []

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if(first[i] == last[i]):
                result.append(first[i])
            else:
                break

        return "".join(result)
