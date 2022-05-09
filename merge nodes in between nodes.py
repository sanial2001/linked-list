# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums, node = 0, head.next
        prev = node
        while head:
            if head.val == 0:
                sums = 0
                head = head.next
            else:
                while head.val != 0:
                    sums += head.val
                    head = head.next
                newnode = ListNode(sums, None)
                prev.next = newnode
                prev = newnode
        return node.next
