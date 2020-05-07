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

    def oddEvenList(self):
        if(self.head is None or self.head.next is None):
            return self
        odd = self.head
        even = self.head.next
        evenHead = even

        while(even is not None and even.next is not None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return odd

    def printList(self):
        l = []
        temp = self.head
        while(temp):
            l.append(temp.val)
            # print(temp.val)
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
    llist.printList()

    llist.oddEvenList()
    llist.printList()


