# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next

        curr, prev = head, None
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt

        return head
