class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        s = []
        s2 = []
        carry = 0
        current = l1
        current2 = l2
        while current:
            s.append(current.val)
            if current.next:
                current = current.next
            else:
                break

        while current2:
            s2.append(current2.val)
            if current2.next:
                current2 = current2.next
            else:
                break
        
        if len(s) > len(s2):
            h  = ListNode(0)
            c = h
            while i < len (s):
                if i < len(s2):
                    if s[i] + s2[i] + carry >= 10:
                        c.next = ListNode(s[i] + s2[i] + carry - 10)
                        carry = 1
                        c = c.next
                        i +=1
                    else:
                        c.next = ListNode(s[i] + s2[i] + carry)
                        carry = 0
                        c = c.next
                        i+=1
                else:
                    if s[i] + carry >= 10:
                        c.next = ListNode(s[i] + carry - 10)
                        carry = 1
                        c = c.next
                        i+=1
                    else:
                        c.next = ListNode(s[i] + carry)
                        carry = 0
                        c = c.next
                        i+=1
            if carry == 1:
                c.next = ListNode(1)
                c = c.next
            return h.next
        else:
            h  = ListNode(0)
            c = h
            while i < len (s2):
                if i < len(s):
                    if s[i] + s2[i] + carry >= 10:
                        c.next = ListNode(s[i] + s2[i] + carry - 10)
                        carry = 1
                        c = c.next
                        i +=1
                    else:
                        c.next = ListNode(s[i] + s2[i] + carry)
                        carry = 0
                        c = c.next
                        i+=1
                else:
                    if s2[i] + carry >= 10:
                        c.next = ListNode(s2[i] + carry - 10)
                        carry = 1
                        c = c.next
                        i+=1
                    else:
                        c.next = ListNode(s2[i] + carry)
                        carry = 0
                        c = c.next
                        i+=1
            if carry == 1:
                c.next = ListNode(1)
                c = c.next
            return h.next
            