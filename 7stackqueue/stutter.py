'''
Given a queue - [1,2,3], return [1,1,2,2,3,3]
'''
import queue

def stutter(q):
    result = []
    while not q.empty():
        item = q.get()
        result.append(item)
        result.append(item)
    print(result)

if __name__ == "__main__":
    q = queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    stutter(q)