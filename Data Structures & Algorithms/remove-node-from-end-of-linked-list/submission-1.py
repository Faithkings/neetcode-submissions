# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        arr.remove(arr[len(arr) - n])

        if not arr:
            return None

        for i in range(len(arr) - 1):
            arr[i].next = arr[i+1]
        
        arr[len(arr) - 1].next = None

        return arr[0]





        
        


        
        
