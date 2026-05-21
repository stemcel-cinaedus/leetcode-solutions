# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dumdum = head
        while dumdum:
            if dumdum in seen:
                return dumdum
            seen.add(dumdum)
            dumdum = dumdum.next


