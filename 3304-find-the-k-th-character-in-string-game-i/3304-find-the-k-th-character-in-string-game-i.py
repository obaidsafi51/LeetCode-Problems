class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(k):
            if k == 1:
                return 'a'
            length = 1

            while length < k:
                length *= 2
            h = length//2

            if k <= h:
                return helper(k)
            else:
                prev_char = helper(k - h)
                return 'a' if prev_char == 'z' else chr(ord(prev_char) + 1)

        return helper(k)