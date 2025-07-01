class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        total_variants = 0
        i = 0

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length >= 2:
                total_variants += (length - 1)
            i = j

        return 1 + total_variants 
