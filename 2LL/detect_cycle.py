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

        return new_node   
    
    def isCycle(self, head):
        s = set()
        temp = head
        
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        
        return False

    # Floyd's Cycle-Finding Algorithm
    def isCycle2(self, head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    llist.head.next.next = llist.head.next

    print(llist.isCycle(llist.head))
    print(llist.isCycle2(llist.head))

