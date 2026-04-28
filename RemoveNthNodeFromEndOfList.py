# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        node = head
        while node:
            node = node.next
            c += 1
        node = head
        pos = 0
        prev = None
        while pos < c - n:
            prev = node
            node = node.next
            pos += 1
        if n == c:
            head = head.next 
        elif prev:
            prev.next = node.next
        else:
            head = None
        
        return head
