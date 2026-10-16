# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()
        r = head

        while r:
            if r.val not in seen:
                seen.add(r.val)
            elif r.val in seen and r.next:
                return True
            r = r.next
        return False
