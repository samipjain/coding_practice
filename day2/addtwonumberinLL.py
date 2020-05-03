class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addTwoNumbers(self, l1, l2):
        prev = None
        temp = None
        carry = 0

        while(l1 is not None or l2 is not None):
            fdata = 0 if l1 is None else l1.data
            sdata = 0 if l2 is None else l2.data
            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10

            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            temp.next = Node(carry)


if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(2)
    second = Node(4)
    third = Node(5)

    llist.head.next = second
    second.next = third
    llist.printList()

    llist2 = LinkedList()

    llist2.head = Node(5)
    second2 = Node(6)
    third2 = Node(4)

    llist2.head.next = second2
    second2.next = third2
    llist2.printList()
    
    output = LinkedList()
    output.addTwoNumbers(llist.head, llist2.head)
    output.printList()
