# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        one, two = head, head.next
        while two and two.next:
            one = one.next
            two = two.next.next
        back = self.rev(one.next)
        one.next = None

        ans = ListNode()
        node = ans
        while head and back:
            ans.next = ListNode(head.val)
            ans = ans.next
            ans.next = ListNode(back.val)
            ans = ans.next
            head, back = head.next, back.next
