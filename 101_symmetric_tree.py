from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_side_deq = deque([root.left])
        right_side_deq = deque([root.right])

        while True:
            left_side = left_side_deq.popleft()
            right_side = right_side_deq.popleft()

            if (left_side is None) != (right_side is None):
                return False

            if left_side and right_side:

                if left_side.val != right_side.val:
                    return False
                        
                left_side_deq.extend([left_side.left, left_side.right])
                right_side_deq.extend([right_side.right, right_side.left])
            
            else:
                if (left_side_deq is None) and (right_side_deq is None):
                    return True