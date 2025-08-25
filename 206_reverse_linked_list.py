from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        next_ = None
        while head:
            item = ListNode(val=head.val, next=next_)
            head = head.next
                
            next_ = item
        return item