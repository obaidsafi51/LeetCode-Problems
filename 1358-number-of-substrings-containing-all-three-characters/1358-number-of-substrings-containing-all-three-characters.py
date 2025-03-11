class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a' : 0, 'b' : 0, 'c' : 0}
        left = 0
        result = 0

        n = len(s)
        
        for right in range(n):
            count[s[right]] += 1

            while all(count[ch] > 0 for ch in 'abc'):
                result += (n - right)
                count[s[left]] -= 1
                left += 1
        return result