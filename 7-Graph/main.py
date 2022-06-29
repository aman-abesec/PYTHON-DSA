Directed Graph:
    Sum of indegree=|E|
    Sum of outdegree=|E|
    Maximum number of edges=|V|(|V|-1)

Indirected Graph:
    Sum of Degree=2*|E|
    Maximum number of edges=|V|*(|V|-1)/2
    Degree=Max number of edges connected to a vertex

# =======================================
# Adjacency List Representation
# ==========================================
from collections import deque
class Graph:
    def __init__(self,size):
        self.size=size
        self.adj=[[] for i in range(self.size)]

    def addedge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def printgraph(self):
        for row in self.adj:
            print(row)

    #BFS for connected Graph
    def bfs(self,s):
        visited=[False]*self.size
        q=deque()
        q.append(s)
        visited[s]=True
        while q:
            s=q.popleft()
            print(s,end=" ")
            for u in self.adj[s]:
                if visited[u]==False:
                    q.append(u)
                    visited[u]=True
    def bfs1(self,s,visited):
        q=deque()
        q.append(s)
        visited[s]=True
        while q:
            s=q.popleft()
            print(s,end=" ")
            for u in self.adj[s]:
                if visited[u]==False:
                    q.append(u)
                    visited[u]=True
    def bfsdis(self):
        #Time Comlacity : O(V+E)
        visited=[False]*self.size
        for u in range(len(self.adj)):
            if visited[u]==False:
                bfs1(u,visited)

v=Graph(5)
v.addedge(0,1)
v.addedge(0,2)
v.addedge(1,2)
v.addedge(1,3)
v.addedge(2,3)
v.addedge(2,4)
v.addedge(3,4)
v.printgraph()
v.bfs(0)

def dfsrec(adj,s,visited):
    visited[s]=True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u]==False:
            dfsrec(adj,u,visited)
def dfs(adj,s):
    visited=[False]*len(adj)
    dfsrec(adj,s,visited)
adj=[[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
dfs(adj,0)
