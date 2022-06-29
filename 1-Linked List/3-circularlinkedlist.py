#==========================================
# Circular linkedlist implementation
#===========================================
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

#=====================================
# Traversal of Circular linked list
#===================================
def traversing(head):
    if head==None:
        return
    print(head.val)
    curr=head.next
    while(curr!=head):
        print(curr.val)
        curr=curr.next

#=============================================
# Insert at beginning of Circular linked list
#===========================================
def insertatbeg(head,key):
    temp=Node(key)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp
    temp.val,head.val=head.val,temp.val
    return head

#=============================================
# Insert at end of Circular linked list
#===========================================
def insertatend(head,key):
    temp=Node(key)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp
    temp.val,head.val=head.val,temp.val
    return head.next


#=============================================
# Delete head of Circular linked list
#===========================================
def delethead(head):
    if head==None or head.next==head:
        return None
    head.val=head.next.val
    head.next=head.next.next
    return head

#=============================================
# Delete kth Node of Circular linked list
#===========================================
def deletekthnode(head,pos):
    if head==None:
        return None
    elif pos==1:
        if head==None or head.next==head:
            return None
        head.val=head.next.val
        head.next=head.next.next
        return head
    curr=head
    for i in range(pos-2):
        curr=curr.next
    curr.next=curr.next.next
    return head


#==================implementation======
head=Node(4)
head.next=Node(5)
head.next.next=Node(6)
head.next.next.next=head
# head=insertatbeg(head,3)
# head=insertatend(head,7)
# head=delethead(head)
head=deletekthnode(head,3)
traversing(head)
