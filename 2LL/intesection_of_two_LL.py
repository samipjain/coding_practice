class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dictA={}
        # step 1: travel headA, and storaged each node in a dict
        while headA:
            dictA[headA] = 0
            headA = headA.next
        # step 2: travel headB, check each node if in dict 
        while headB:
            # if checked, return the headB node = intersctionNode
            if headB in dictA:
                return headB
            headB = headB.next
        #No checked, no found intersctionNode
        return None