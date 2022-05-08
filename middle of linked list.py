# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp is not None:
            n += 1
            temp = temp.next

        i = 0
        while head is not None:
            if i == n // 2:
                return head
            i += 1
            head = head.next
