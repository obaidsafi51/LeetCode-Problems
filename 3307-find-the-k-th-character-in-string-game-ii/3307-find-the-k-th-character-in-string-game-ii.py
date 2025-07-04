class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
       
        m = len(operations)
        L = [1] * (m + 1)
        for i in range(1, m + 1):
            L[i] = L[i - 1] * 2
            if L[i] > k:
                L[i] = k + 1  

        shifts = 0
        for i in range(m, 0, -1):
            half = L[i - 1]
            if k > half:
                k -= half
                if operations[i - 1] == 1:
                    shifts = (shifts + 1) % 26

        return chr((ord('a') - ord('a') + shifts) % 26 + ord('a'))
