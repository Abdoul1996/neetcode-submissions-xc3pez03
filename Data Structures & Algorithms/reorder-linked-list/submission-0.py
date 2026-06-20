# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # step 1 : Find Middle and Splits 

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None 

        # Step 2 : Reverse the Second Half 

        prev, cur = None, second 

        while cur:
            nxt = cur.next
            cur.next = prev 
            prev = cur
            cur = nxt
        second = prev 

        # Step 3 : Merge two halves, and alternates 

        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second 
            second.next = tmp1
            first = tmp1
            second = tmp2
        