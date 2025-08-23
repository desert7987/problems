class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        zero_idxs = []
        
        for i, num in enumerate(nums):
            if num == 0:
                zero_idxs.append(i)

        zero_idxs.reverse()

        for idx in zero_idxs:
            del nums[idx]
            nums.append(0)
