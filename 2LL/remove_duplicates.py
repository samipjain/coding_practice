class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        
        curr = head
        move = curr.next
        
        while curr.next:    
            if move.val == curr.val:
                curr.next = move.next
                move = move.next
            else:
                curr = curr.next
                move = move.next
        return head