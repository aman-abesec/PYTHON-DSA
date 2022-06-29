#=====================================
# Queue implementation
#====================================
# Using List
# from collections.deque
# Using queue.Queue


#=====================================
# Queue implementation using List
#====================================
Queue=[]
Queue.append(10)
Queue.append(20)
Queue.pop(0)
len(Queue)
Queue[0]
Queue[-1]

#=====================================
# Queue implementation using deque
#====================================
from collections import deque
q=deque()
q.append(10)
q.append(20)
q.popleft()
len(q)
q[0]
q[-1]

#=======================================
# Queue implementation using Linkedlist
#=======================================
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def length(self):
        return self.size
    def isempty(self):
        return self.size==0
    def getfront(self):
        return self.front.val
    def getrear(self):
        return self.rear.val
    def enque(self,val):
        temp=Node(val)
        if self.size==0:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size+=1
    def deque(self):
        if self.front==None:
            return math.inf
        else:
            value=self.front.val
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.size-=1
            return value
q=Queue()
q.enque(10)
q.enque(20)
print(q.length())
print(q.getfront())
print(q.getrear())
print(q.deque())
