"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = 0
        new_l_map = {}
        copy = head
        while copy:
            new_l_map[copy] = Node(copy.val)
            copy = copy.next
        pos = head
        while pos:
            if pos.random in new_l_map:
                new_l_map[pos].random = new_l_map[pos.random]
            else:
                new_l_map[pos].random = None
            if pos.next:
                new_l_map[pos].next = new_l_map[pos.next]
            pos = pos.next
        return new_l_map[head]
