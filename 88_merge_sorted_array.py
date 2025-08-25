from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        limit_nums_2 = nums2[:n]
        del nums1[m:]

        nums1.extend(limit_nums_2)
        nums1.sort()