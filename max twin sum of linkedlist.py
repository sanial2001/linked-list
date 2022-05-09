# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ans, i, j = 0, 0, n - 1
        while i < j:
            ans = max(ans, nums[i] + nums[j])
            i, j = i + 1, j - 1
        return ans
