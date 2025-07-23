class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, first, second, score):
            stack = []
            gain = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    gain += score
                else:
                    stack.append(ch)
            return "".join(stack), gain

        total = 0
        if x >= y:
           
            s, gain = remove_pattern(s, 'a', 'b', x)
            total += gain
            s, gain = remove_pattern(s, 'b', 'a', y)
            total += gain
        else:
            
            s, gain = remove_pattern(s, 'b', 'a', y)
            total += gain
            s, gain = remove_pattern(s, 'a', 'b', x)
            total += gain
        return total