class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            r_t = 0
            r_b = 0

            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x :
                    return -1
                elif tops[i] != x:
                    r_t +=1
                elif bottoms[i] != x:
                    r_b += 1
            return min(r_t, r_b)

        result = check(tops[0])

        if result != -1:
            return result 
        elif tops[0] != bottoms[0]:
            return check(bottoms[0])
        else:
            return -1