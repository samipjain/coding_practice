class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        
        prev = None
        curr = head
        n = curr.next
        
        
        while curr.next:
            curr.next = prev
            prev = curr
            curr = n
            n = n.next
        curr.next = prev
        
        return curr

    def reverseListUsingRecursion(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If head is empty or has reached the list end 
        if head is None or head.next is None: 
            return head 
  
        # Reverse the rest list 
        rest = self.reverseList(head.next) 
  
        # Put first element at the end 
        head.next.next = head 
        head.next = None
  
        # Fix the header pointer 
        return rest