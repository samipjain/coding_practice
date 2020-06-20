class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Iterate over and store the values in a list
        curr = head
        ll_list = []
        while(curr):
            ll_list.append(curr.val)
            curr = curr.next
        
        # keeping two variables - front and rear 
        # Iterate over list until front != rear
        # If any values differ then it is not a palindrome
        front = 0
        rear = len(ll_list) - 1
        
        while front < rear:
            if ll_list[front] != ll_list[rear]:
                return False
            front += 1
            rear -= 1
        return True