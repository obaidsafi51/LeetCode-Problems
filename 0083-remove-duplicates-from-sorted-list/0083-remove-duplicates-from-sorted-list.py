# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = prev = head

        while cur.next is not None: 
            cur = cur.next
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
        return head