class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        left, right = 1, min(ranks) * cars * cars  

        def canRepairInTime(T):
            total_cars = 0
            for r in ranks:
                total_cars += int(math.sqrt(T // r))  
                if total_cars >= cars: 
                    return True
            return total_cars >= cars
        
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  
            else:
                left = mid + 1  
        
        return left  