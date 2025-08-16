class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(x):
            return sum(int(digit) **2 for digit in str(x)) 

        slow = n
        fast = sum_of_squares(n)

        while n != 1 and slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

        return fast == 1