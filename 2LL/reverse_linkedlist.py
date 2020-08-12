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

    
    
    def reverse(self, head):
        if head is None:
            return
    
        prev = None
        n = head.next
        curr = head
        while curr.next != None:
            curr.next = prev
            prev = curr
            curr = n
            n = n.next
            
        curr.next = prev
        while curr is not None:
            print(curr.val, end="\n")
            curr = curr.next

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.reverse(llist.head)

