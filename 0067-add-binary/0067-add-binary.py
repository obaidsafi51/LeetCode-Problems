class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i , j = len(a)-1, len(b)-1
        carry = 0 
        result = []
        while i >= 0 or j >= 0 or carry:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            result.append(str(sum % 2))

            carry = sum // 2
        return ''.join(result[::-1]) 
