class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, n):
        self.n = n
        self.nodes = {}
        self.count = 0
        self.head = None

    def set(self, key, value):
        # If node exists then update the value and move it to front
        if key in self.nodes:
            self.nodes[key] = value
            # Move to front
        
        # No space, so remove last item
        if self.count == self.n:
            # Remove last node
            del self.nodes[self.end.key]
            self.remove(self.end)
        else:
            self.count += 1

        # Create the node
        node = Node(key, value)
        self.insert(node)
        self.nodes[key] = node
        self.printDLL()
        # print(self.nodes)
        

    def get(self, key):
        if key not in self.nodes:
            return

        node = self.nodes[key]
        self.move_to_end(node)
        return node.val

    def insert(self, node):
        # insert the first node
        if self.head is None:
            self.head = node
            self.end = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def remove(self, node):
        if self.end is None:
            print("No nodes in cache")
            return
        
        # If only one node
        if self.head == self.end:
            self.head = None
            self.end = None
        elif node.next is None: # Last node
            curr = node.prev
            node.prev = None
            curr.next = None
            self.end = curr
        elif node.prev is None: # First node
            self.head = node.next
            self.head.prev = None
            node.next = None
        else:
            curr = node.prev
            curr.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

    def move_to_end(self, node):
        self.remove(node)
        self.insert(node)

    def printDLL(self):
        if self.head is None:
            return
        curr = self.head
        while(curr):
            print("key", curr.key)
            curr = curr.next
        print('---------')

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set('user1', 'Alex')
    cache.set('user2', 'Brian')
    print(cache.get('user1'))
    cache.printDLL()
    cache.set('user3', 'Chris')
    print(cache.get('user1'))
    cache.printDLL()
    cache.set('user4', 'Samip')
    print(cache.get('user1'))

    