class Solution:
    def sieve_of_eratosthenes(self, n : int) -> List[int]:
        is_prime = [True] * (n +1)
        is_prime[0] = False
        is_prime[1] = False

        p = 2 

        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p*p, n+1, p):
                    is_prime[multiple] = False
            p += 1
        return is_prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]
        
        left  = max(left, 2)

        is_prime = self.sieve_of_eratosthenes(right)
        
        prime = []
        for num in range(left, right+1):
            if is_prime[num]:
                prime.append(num)
        if len(prime) < 2:
            return [-1,-1]
        
        best_pair= [-1,-1]
        min_diff = float('inf')

        for i in range(len(prime)-1):
            diff = prime[i+1] - prime[i]
            if diff < min_diff :
                min_diff = diff
                best_pair = [prime[i], prime[i+1]]
        
        return best_pair
