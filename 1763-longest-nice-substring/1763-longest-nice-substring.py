class Solution:
    def Recursive(self, sub:str) -> str:
        
        if len(sub) < 2:
            return ""
        
        letters = set(sub)

        for i,ch in enumerate(sub):
            if ch.swapcase() not in letters:
                left = self.Recursive(sub[:i])
                right = self.Recursive(sub[i+1:])

                return left if len(left) >= len(right) else right
            
        return sub

    def longestNiceSubstring(self, s: str) -> str:

        return self.Recursive(s)

    


