# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = -1
        temp = head
        while temp is not None:
            n += 1
            temp = temp.next

        if n == 0:
            return None

        mid = n // 2 if n % 2 == 0 else (n // 2) + 1
        node = head
        prev = None
        i = 0
        while node is not None:
            if i == mid:
                prev.next = node.next
                del node
                return head
            prev = node
            node = node.next
            i += 1
