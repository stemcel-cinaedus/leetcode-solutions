# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# First idea:
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         seen = set()
#         dumdum = head
#         while dumdum:
#             if dumdum in seen:
#                 return dumdum
#             seen.add(dumdum)
#             dumdum = dumdum.next

#Second idea:

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slowp, fastp = head, head
#         while fastp and fastp.next:
#             fastp = fastp.next.next
#             if fastp == slowp:
#                 markerp = head
#                 while fastp:
#                     fastp = fastp.next
#                     if fastp == markerp:
#                         return markerp
#                     if fastp == slowp:
#                         markerp = markerp.next
#             slowp = slowp.next

# Second idea improved:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowp, fastp = head, head
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if fastp == slowp:
                while slowp != head:
                    head = head.next
                    slowp = slowp.next
                return head
        return None
