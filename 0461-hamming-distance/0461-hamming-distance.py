class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x^y
        count = 0
        while xor_result > 0:
            count += xor_result & 1
            xor_result >>= 1
        return count