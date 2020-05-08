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

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()