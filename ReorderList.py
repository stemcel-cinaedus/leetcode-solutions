# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        whole, half = head, head
        while whole and whole.next:
            whole = whole.next.next
            half = half.next
        
        right = half.next
        half.next = None
        prev = None
        while right:
            next_node = right.next
            right.next = prev
            prev = right
            right = next_node
        
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next, second.next = second, t1
            first, second = t1, t2

