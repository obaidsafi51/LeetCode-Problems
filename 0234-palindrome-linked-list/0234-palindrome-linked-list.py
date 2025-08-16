# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversedList(self , slow : Optional[ListNode]) -> [List]:
        head = slow
        prev = None
        cur = head 
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reversedList(slow)
        first_half = head

        while second_half:
            if second_half.val != first_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
         
        return True
