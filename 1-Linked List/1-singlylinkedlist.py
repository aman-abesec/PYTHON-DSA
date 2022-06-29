#============================================
#     Simple linked list implementation
#=============================================
class Node:
    def __init__(self,k):
        self.val=k
        self.next=None


#=========================================
# Traversing in a linked list
#=========================================
#==============Method-1======
def Traversing(head):
    curr=head
    while(curr):
        print(curr.val)
        curr=curr.next
#===============Method-2=======
def recTraversing(head):
    if head==None:
        return
    print(head.val)
    recTraversing(head.next)

#=========================================
# Searching in a linked list
#=========================================
def search(head,k):
    c=1
    curr=head
    while curr:
        if curr.val==k:
            return c
        c+=1
        curr=curr.next
    return -1

#============================================
#     Insertion at Bigenning
#=============================================
def insertatbeg(head,key):
    temp=Node(key)
    temp.next=head
    return temp

#============================================
#     Insertion at End
#=============================================
def insertatend(head,key):
    curr=head
    if curr==None:
        return Node(key)
    while(curr.next!=None):
        curr=curr.next
    curr.next=Node(key)
    return head


#============================================
#     Insertion at given position
#=============================================
def insertatpos(head,key,pos):
    curr=head
    temp=Node(key)
    if pos==1:
        temp.next=head
        return temp
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head

#============================================
#     Delete First node of Linkedlist
#=============================================
#Note:> Python don't required memory deallocation
def deletefirstnode(head):
    if head==None:
        return  head
    return head.next

#============================================
#     Delete Last node of Linkedlist
#=============================================
def deletelastnode(head):
    if head==None or head.next==None:
        return None
    curr=head
    while(curr.next.next!=None):
        curr=curr.next
    curr.next=None
    return head

#=================================================
# Sorted Insert in a linked List
#=================================================
def sortedinsert(head,key):
    temp=Node(key)
    if head==None:
        return temp
    if head.val>=key:
        temp.next=head
        return temp
    curr=head
    while(curr.next!=None and curr.next.val<key):
        curr=curr.next
    temp.next=curr.next
    curr.next=temp
    return head

#=================================================
# Reverse a linked List
#=================================================
#Note:> You can also reverse by using a list
#==========Method-1=======
def reverselinkedlist(head):
    curr=head
    prev=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev
#==========Method-2===========
def recursivereverse(curr,prev=None):
    if curr==None:
        return prev
    next=curr.next
    curr.next=prev
    return recursivereverse(next,curr)


#=========Method-1========
head=Node(5)
temp1=Node(6)
temp2=Node(7)
temp3=Node(8)
head.next=temp1
temp1.next=temp2
temp2.next=temp3
#=============Method-2=======
temp=Node(1)
# temp.next=Node(2)
# temp.next.next=Node(3)
# recTraversing(temp)
# print(search(head,8))
# head=insertatbeg(head,4)
# head=insertatend(head,9)
# head=insertatpos(head,10,3)
# head=deletefirstnode(head)
# head=deletelastnode(temp)
# head=sortedinsert(temp,90)
head=reverselinkedlist(head)
Traversing(head)
