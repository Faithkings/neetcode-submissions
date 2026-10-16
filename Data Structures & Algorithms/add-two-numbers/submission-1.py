# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # values = []
        # l1_val = l1
        # l2_val = l2
        # carry = 0

        # while l1 or l2 or carry:
        #     nxt1 = l1.next
        #     nxt2 = l2.next
        #     lsum = l1.val + l2.val + carry
        #     if lsum >= 10:
        #         values.append(lsum-10)
        #         carry = 1
        #     else:
        #         values.append(lsum)
        #         carry = 0
        #     l1 = nxt1
        #     l2 = nxt2
        # dummy = ListNode()
        # current = dummy

        # for val in values:
        #     current.next = ListNode(val)
        #     current = current.next

        # return dummy.next

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next