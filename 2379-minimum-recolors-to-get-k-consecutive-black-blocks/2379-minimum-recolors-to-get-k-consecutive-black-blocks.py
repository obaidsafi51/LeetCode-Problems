class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        if k > n:
            return -1  

        current_black_count = sum(1 for i in range(k) if blocks[i] == 'B')
        max_black_count = current_black_count

        for i in range(k, n):
            if blocks[i - k] == 'B':
                current_black_count -= 1
            if blocks[i] == 'B':
                current_black_count += 1

            max_black_count = max(max_black_count, current_black_count)

        return k - max_black_count