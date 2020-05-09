class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.queue = [None for i in range(k)]
        self.rear = self.front = -1       

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if ((self.rear + 1) % self.k == self.front):
            return False
        elif (self.rear == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if (self.front == -1):
            return False
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return True
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k  
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if (self.front == -1):
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if (self.rear == -1):
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.queue == []
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.rear+1 == self.k
    
    def print(self):
       # condition for empty queue 
        if(self.front == -1):
            print ("Queue is Empty")
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.k): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.k == self.front): 
            print("Queue is Full") 

if __name__ == "__main__":

    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    obj.enQueue(1)
    obj.print()
    obj.enQueue(2)
    obj.print()
    obj.enQueue(3)
    obj.print()
    obj.deQueue()
    obj.print()
    print(obj.isEmpty())
    print(obj.isEmpty())
    print(obj.Rear())
    obj.enQueue(4)
    obj.print()