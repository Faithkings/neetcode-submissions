# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # arr = []
        # while head:
        #     arr.append(head)
        #     head = head.next
        # arr.remove(arr[len(arr) - n])

        # if not arr:
        #     return None

        # for i in range(len(arr) - 1):
        #     arr[i].next = arr[i+1]
        
        # arr[len(arr) - 1].next = None

        # return arr[0]


        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
            



        
        


        
        
