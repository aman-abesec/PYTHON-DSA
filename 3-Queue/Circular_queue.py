#=====================================
# Circular Queue implementation using List
#====================================
class Cqueue:
    def __init__(self,c):
        self.l=[None]*c
        self.capacity=c
        self.size=0
        self.front=0
    def getfront(self):
        if self.size==0:
            return None
        else:
            return self.l[self.front]
    def getrear(self):
        if self.size==0:
            return None
        else:
            rear=(self.front+self.size-1)%self.capacity
            return self.l[rear]

    def enque(self,x):
        if self.size==self.capacity:
            return
        else:
            rear=(self.front+self.size-1)%self.capacity
            rear=(rear+1)%self.capacity
            self.l[rear]=x
            self.size+=1

    def deque(self):
        if self.size==0:
            return None
        else:
            res=self.l[self.front]
            self.front=(self.front+1)%self.capacity
            self.size-=1
            return res
q=Cqueue(5)
q.enque(4)
q.enque(6)
print(q.getfront())
q.deque()
print(q.getrear())
