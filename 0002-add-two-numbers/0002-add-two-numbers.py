# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # Dummy node to simplify edge cases
        curr = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add digits and carry
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)  # Only the remainder stays as digit
            curr = curr.next

            # Move forward in both lists if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next