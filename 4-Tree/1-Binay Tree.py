#=====================================
# Binary Tree implementation
#====================================
class Tree:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

#=====================================
# Inorder Traversal Recursive
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def inordertraversal(root):
    if root!=None:
        inordertraversal(root.left)
        print(root.val,end=" ")
        inordertraversal(root.right)

#=====================================
# Pre Traversal Recursive
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def preordertraversal(root):
    if root!=None:
        print(root.val,end=" ")
        preordertraversal(root.left)
        preordertraversal(root.right)

#=====================================
# postorder Traversal Recursive
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def postordertraversal(root):
    if root!=None:
        postordertraversal(root.left)
        postordertraversal(root.right)
        print(root.val,end=" ")

# Note :> All choose Inorder or Preorder Traversal
# because they are Tail recursive.

#=====================================
# Size of a Binary Tree
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def size(root):
    if root==None:
        return 0
    return 1+size(root.left)+size(root.right)


#=====================================
# Maximum in a Binary Tree
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
import math
def maxvalue(root):
    if root==None:
        return -math.inf
    return max(root.val,maxvalue(root.left),maxvalue(root.right))

#=====================================
# Search in a Binary Tree
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def ispresent(root,ele):
    if root==None:
        return False
    elif root.val==ele:
        return True
    elif ispresent(root.left,ele)==True:
        return True
    else:
        return ispresent(root.right,ele)

#=====================================
# Height of a Binary Tree
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))

#=====================================
# Inorder Traversal Iterative Method
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def inordertraversaliter(root):
    stack=[]
    if root==None:
        return
    temp=root
    while temp!=None:
        stack.append(temp)
        temp=temp.left
    while len(stack)>0:
        curr=stack.pop()
        print(curr.val,end=" ")
        temp=curr.right
        while temp!=None:
            stack.append(temp)
            temp=temp.left

#=====================================
# Preorder Traversal Iterative Method
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : 0(height of tree)
def preordertraversaliter(root):
    stack=[root]
    if root==None:
        return
    while(len(stack)>0):
        temp=stack.pop()
        print(temp.val,end=" ")
        if temp.right!=None:
            stack.append(temp.right)
        if temp.left!=None:
            stack.append(temp.left)

#=====================================
#Level Order Traversal
#====================================
#Time Complexity : 0(n)
#Auxilary Space  : O(n)
def levelorder(root):
    if root==None:
        return
    queue=[]
    queue.append(root)
    while len(queue)>0:
        temp=queue.pop(0)
        print(temp.val,end=" ")
        if temp.left!=None:
            queue.append(temp.left)
        if temp.right!=None:
            queue.append(temp.right)
#==========implementation====
root=Tree(10)
root.left=Tree(20)
root.right=Tree(30)
root.left.left=Tree(40)
root.left.right=Tree(70)
root.right.left=Tree(60)
# inordertraversal(root)
# print()
# preordertraversal(root)
# print()
# postordertraversal(root)
# print(size(root))
# print(maxvalue(root))
# print(ispresent(root,60))
# print(height(root))
# inordertraversaliter(root)
# preordertraversaliter(root)
levelorder(root)
