# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr, prev = list1, None
        l1, l2 = None, None
        index = 0
        while curr:
            if index == a:
                l1 = prev
            if index == b:
                l2 = curr.next
            prev = curr
            curr = curr.next
            index += 1

        l1.next = list2
        curr = list2
        while curr:
            if curr.next == None:
                curr.next = l2
                break
            curr = curr.next

        return list1
