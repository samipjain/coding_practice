class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList():
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
    
    def removeCycle(self, head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow == fast:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None

        temp = head
        while temp:
            print(temp.data, end="\n")
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.head.next.next.next.next.next = ll.head.next

    ll.removeCycle(ll.head)