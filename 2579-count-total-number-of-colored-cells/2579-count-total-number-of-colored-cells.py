class Solution:
    def coloredCells(self, n: int) -> int:
        result = (2*n*n) - 2*n + 1
        return result