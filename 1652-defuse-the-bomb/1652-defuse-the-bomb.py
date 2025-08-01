class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        window = 0
        if k > 0:
            for j in range(1, k+1):
                window += code[j % n]
        else:
            for j in range(n+k, n):
                window += code[j % n]

        for i in range(n):
            res[i] = window
            if k > 0:
                window += code[(i + k + 1) % n]
                window -= code[(i + 1)     % n]
            else:
                window += code[i % n]
                window -= code[(i + k) % n]

        return res