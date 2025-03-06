class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_num = n * n 

        es = (total_num*(total_num + 1)) // 2
        ess = (total_num*(total_num+1)*(2*total_num + 1 )) //6

        actualSum = 0
        actualSumSquares = 0
        
        for row in grid:
            for num in row:
                actualSum += num
                actualSumSquares += num * num

        delta = actualSum - es
        delta2 = actualSumSquares - ess

        sum_ab = delta2 // delta 

        a = (sum_ab + delta)//2
        b = sum_ab - a
         
        return [a,b]