class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        base10_str = ''
        curr = head
        
        while(curr is not None):
            base10_str = base10_str + str(curr.val)
            curr = curr.next
        return int(base10_str, 2)