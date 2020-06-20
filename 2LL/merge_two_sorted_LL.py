class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            result = l1
            l1 = l1.next
        else:
            result = l2
            l2 = l2.next
        
        curr = result
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1 is None:
            curr.next = l2
        if l2 is None:
            curr.next = l1
        return result