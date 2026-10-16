# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
    
        # arr = []

        # while head:
        #     arr.append(head)
        #     head = head.next
        # l = 0
        # r = len(arr) - 1
        # while l < r:
        #     arr[l].next = arr[r]
        #     l += 1
        #     if l >= r:
        #         break
        #     arr[r].next = arr[l]
        #     r -= 1
        # arr[l].next = None
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #merge two halves
        first, second = head, prev
        while second and first:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

           
        


        
        

