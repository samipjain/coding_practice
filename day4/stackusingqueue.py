class Queue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        return self.queue == []
        
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.curr_size += 1
        
        self.q2.put(x)

        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if (self.q1.empty()):
            return
        
        self.curr_size -= 1        
        return self.q1.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.empty()

if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param2 = obj.pop()
    print(param2)

    param3 = obj.top()
    print(param3)
    
    param4 = obj.empty()
    print(param4)

    print(obj.pop())
    print(obj.empty())