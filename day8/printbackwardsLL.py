class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        
        if (self.head is None):
            self.head = new_node
            return

        temp = self.head 
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    def printList(self):
        result = []
        temp = self.head
        while(temp):
            result.append(temp.val)
            temp = temp.next
        print(result)

    def printBackwards(self):
        result = []
        temp = self.head
        while(temp):
            result.append(temp.val)
            temp = temp.next
        
        while(result):
            print(result.pop())

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.printList()
    ll.printBackwards()