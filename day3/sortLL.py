class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        # If linked list is empty
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def sortList(self, head):
        # Base case
        if (head is None or head.next is None):
            return head
        
        # Get middle node
        middle = self.getMiddle(head)
        temp = middle.next

        middle.next = None

        left = self.sortList(head)
        right = self.sortList(temp)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if (head == None):
            return head
        
        slow = head
        fast = head
        while(fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
        return slow

    def printList(self, head):
        l = []
        if (head is None):
            print(l)
            return
        temp = head
        while(temp):
            l.append(temp.val)
            temp = temp.next
        print(l)

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(2) 
    llist.append(1) 
    llist.append(3) 
    llist.append(5) 
    llist.append(6) 
    llist.append(4)
    llist.append(7) 
    llist.printList(llist.head)

    llist.head = llist.sortList(llist.head)
    llist.printList(llist.head)


