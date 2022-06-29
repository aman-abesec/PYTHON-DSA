#=====================================
# Implementation of doubly linked list
#=======================================
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

#=====================================
# Traversing of doubly linked list
#=======================================
def traversing(head):
    curr=head
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.next

#=====================================
# Insertion at beginning of doubly linked list
#=======================================
def insertatbeg(head,key):
    temp=Node(key)
    if head==None:
        return temp
    temp.next=head
    head.prev=temp
    return temp


#=====================================
# Insertion at end of doubly linked list
#=======================================
def insertatend(head,key):
    temp=Node(key)
    if head==None:
        return temp
    curr=head
    while(curr.next!=None):
        curr=curr.next
    curr.next=temp
    temp.prev=curr
    return head


#=====================================
# delete head of doubly linked list
#=======================================
def deletehead(head):
    if head==None or head.next==None:
        return None
    head=head.next
    head.prev=None
    return head

#=====================================
# delete end of doubly linked list
#=======================================
def deleteend(head):
    if head==None or head.next==None:
        return None
    curr=head
    while(curr.next.next!=None):
        curr=curr.next
    curr.next=None
    return head

#=====================================
# Reverse a doubly linked list
#=======================================
def reverse(head):
    if head==None or head.next==None:
        return head
    curr=head
    prev=None
    while(curr!=None):
        prev=curr
        curr.next,curr.prev=curr.prev,curr.next
        curr=curr.prev
    return prev
#===============implementation===
head=Node(8)
temp1=Node(9)
temp2=Node(10)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
# head=insertatbeg(head,7)
# head=insertatend(head,12)
head=reverse(head)
traversing(head)
