# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                newnode = ListNode(list1.val)
                node.next = newnode
                node = newnode
                list1 = list1.next
            else:
                newnode = ListNode(list2.val)
                node.next = newnode
                node = newnode
                list2 = list2.next

        while list1:
            newnode = ListNode(list1.val)
            node.next = newnode
            node = newnode
            list1 = list1.next
        while list2:
            newnode = ListNode(list2.val)
            node.next = newnode
            node = newnode
            list2 = list2.next

        return head.next
