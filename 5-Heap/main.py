#=======================================
# Heap in Python
#=========================================
import heapq
pq = [5, 20, 1, 30, 4]
heapq.heapify(pq)  # [1,4,5,30,20]
heapq.heappush(pq, 3)  # 1,4,3,30,20,5
print(heapq.heappop(pq))  # [3,4,5,30,20]
print(heapq.nlargest(2, pq))
print(heapq.nsmallest(2, pq))
print(heapq.heapreplace(pq,-1))
print(pq)


#==============================================
#    Heap Implementation
#=============================================
import math
class Heap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return (i-1)//2
    def lchild(self,i):
        return (2*i+1)
    def rchild(self,i):
        return (2*i+2)
    def insert(self,key):
        #Time Complexity O(log(n))
        arr=self.arr
        arr.append(x)
        i=len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p
    def heapify(self,i):
        arr=self.arr
        lt=self.lchild(i)
        rt=self.rchild(i)
        smallest=i
        n=len(arr)
        if lt<n and arr[lt]<arr[smallest]:
            smallest=lt
        if rt<n and arr[rt]<arr[smallest]:
            smallest=rt
        if smallest!=i:
            arr[smallest],arr[i]=arr[i],arr[smallest]
            self.heapify(smallest)

    def extractmin(self):
        curr=self.arr
        n=len(arr)
        if n==0:
            return -math.inf
        res=arr[0]
        arr[0]=arr[n-1]
        arr.pop()
        self.heapify(0)
        return res

    def decreasekey(self,i,x):
        # o(log(n))
        arr=self.arr
        arr[i]=x
        while i!=0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p

    def delete(self,i):
        n=len(self.arr)
        if i>=n:
            return
        else:
            self.decreasekey(i,-math.inf)
            self.extractmin()
