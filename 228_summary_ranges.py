class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        result = []
        half = None
        seq = False

        for idx, num in enumerate(nums):
            if (num - 1) != nums[idx-1]:
                if half:
                    if seq:
                        half += f"->{nums[idx-1]}"
                        seq = False
                    result.append(half)
                half = str(num)
            else:
                seq = True
        if seq:
            half += f"->{nums[-1]}"
        result.append(half)
        
        return result
    