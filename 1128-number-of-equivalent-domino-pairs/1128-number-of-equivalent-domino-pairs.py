class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        pairs = 0

        for a , b in dominoes:

            key = (a,b) if a<=b else (b,a)

            pairs += count[key]

            count[key] += 1

        return pairs