from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(len(intervals)):
            if not merged_intervals:
                merged_intervals.append(intervals[i])
                continue

            old_first = merged_intervals[-1][0]
            old_second = merged_intervals[-1][1]

            new_first = intervals[i][0]
            new_second = intervals[i][1]

            if old_first > new_first and old_first > new_second:
                merged_intervals.insert(-1, intervals[i])

            elif old_second >= new_first:
                first = old_first if old_first <= new_first else new_first
                second = old_second if old_second >= new_second else new_second

                merged_intervals[-1] = [first, second]

            else:
                merged_intervals.append(intervals[i])
            
        return merged_intervals