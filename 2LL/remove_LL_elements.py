class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return
        
        curr = head
        prev = None
        
        # Using prev pointer
        while curr:
            if curr.val == val:
                if prev is None:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # Checking the next value
        if head is None:
            return
        
        curr = ListNode(-1)
        curr.next = head
        
        while curr.next:
            if curr.next.val == val:
                if curr.next == head:
                    head = head.next
                else:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return head