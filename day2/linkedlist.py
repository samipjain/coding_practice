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
    
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

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
    
    def insertAfter(self, value, new_data):
        if self.head is None:
            return

        new_node = Node(new_data)
        temp = self.head

        while(temp.data != value):
            temp = temp.next
            if (temp.next is None):
                break
        
        if (temp.next is None):
            return
        else:
            new_node.next = temp.next
            temp.next = new_node        

    def deleteNode(self, value):
        temp = self.head

        # Head node
        if (temp is not None):
            if (temp.data == value):
                self.head = temp.next
                temp = None
                return
        
        while(temp is not None):
            if (temp.data == value):
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next
        temp = None

if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(0)

    llist.append(4)
    llist.append(5)

    llist.insertAfter(3, 8)
    llist.insertAfter(1, 7)
    llist.insertAfter(7, 9)

    llist.deleteNode(9)
    llist.deleteNode(7)
    llist.deleteNode(8)
    llist.printList()