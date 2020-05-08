class Stack:
    def __init__(self):
        self.stack = []
    
    def put(self, x):
        self.stack.append(x)
    
    def get(self):
        if len(self.stack) < 0:
            return None
        return self.stack.pop(-1)
    
    def empty(self):
        return self.stack == []
    
    def print(self):
        print(self.stack)

if __name__ == "__main__":
    s = Stack()
    s.put(1)
    s.put(2)
    s.put(3)
    s.print()