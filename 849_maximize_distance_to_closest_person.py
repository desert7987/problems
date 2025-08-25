from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = True
        count = 0
        distance = {'max': 1}

        for seat in seats:
            if seat == 0:
                if start:
                    count += 2
                else:
                    count += 1  
                        
                if count > distance['max']:
                    distance['max'] = count
            else:
                start = False
                count = 0

        result = (distance['max'] + 2 - 1) // 2

        if count > result: return count

        return result