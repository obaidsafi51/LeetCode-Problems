class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")

        if x == 0 or x == 1:
            return x
                    
        guess = x / 2
        while True:
            next_guess = (guess + x / guess) / 2
            if int(guess) == int(next_guess):
                return int(next_guess)
            guess= next_guess