#======================================
# Implementation of BSTree
#=========================================
class BSTree:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


#======================================
# Searching in Binary search Tree Recursive
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(height of tree)
def search(root,key):
    if root==None:
        return False
    else:
        if root.val==key:
            return True
        elif root.val<key:
            return search(root.right,key)
        else:
            return search(root.left,key)

#======================================
# Searching in Binary search Tree itre
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(1)
def searchiter(root,key):
    while root!=None:
        if root.val==key:
            return True
        elif root.val<key:
            root=root.right
        else:
            root=root.left
    return False


#======================================
# Insertion in Binary search Tree
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(height of tree)
def insert(root,key):
    if root==None:
        return BSTree(key)
    elif root.val==key:
        return root
    elif root.val>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

#======================================
# Insertion in Binary search Tree Iterative
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(1)
def insertiter(root,key):
    parent=None
    curr=root
    while curr!=None:
        parent=curr
        if curr.val==key:
            return root
        elif curr.val<key:
            curr=curr.left
        else:
            curr=curr.right
    if parent==none:
        return Node(key)
    if parent.val>key:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    return root

#=========================================
# Deletion in Binary search Tree
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(height of tree)
def getSucc(curr,key):
    while curr.left!=None:
        curr=curr.left
    return curr.key
def delete(root,key):
    if root==None:
        return
    if root.val>key:
        root.left=delete(root.left,key)
    elif root.val<key:
        root.right=delete(root.right,key)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            v=getSucc(root.right,key)
            root.val=v
            root.right=delete(root.right,v)
    return root

#=========================================
# Floor in Binary search Tree
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(1)
def floorbst(root,key):
    temp=None
    while root:
        if root.val>key:
            root=root.left
        elif root.val<key:
            temp=root
            root=root.right
        else:
            return root
    return temp

#=========================================
# Ceiling in Binary search Tree
#=========================================
#Time Complexity : 0(height of tree)
#Auxilary Space  : 0(1)
def ceiling(root,key):
    curr=None
    while root:
        if root.val==key:
            return root
        elif root.val<key:
            root=root.right
        else:
            curr=root
            root=root.left
    return curr
def trave(root):
    if root!=None:
        trave(root.left)
        print(root.val)
        trave(root.right)
#=========================================
# Searching in Binary search Tree
#=========================================
root=BSTree(40)
root.left=BSTree(20)
root.right=BSTree(80)
root.left.left=BSTree(8)
root.left.right=BSTree(30)
root.right.left=BSTree(60)
root.right.right=BSTree(100)
root=insert(root,120)
# print(search(root,400))
head=delete(root,8)
print(floorbst(root,10))
trave(root)
