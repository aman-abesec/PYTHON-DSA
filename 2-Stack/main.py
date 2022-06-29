#=====================================
# stack implementation
#===============================
#===========Method-1========
#Note:> All list operation work on  deque
# from collections import deque
# Stack=deque()
#==============Method-2=========
# Stack=[]

#=========================================
# Stack implementation using linked list
#=============================================
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,key):
        temp=Node(key)
        temp.next=self.head
        self.head=temp
        self.size+=1
    def length(self):
        return self.size
    def peek(self):
        if self.head!=None:
            return self.head.val
        return math.inf
    def pop(self):
        if self.head==None:
            return math.inf
        self.size-=1
        value=self.head.val
        self.head=self.head.next
        return value
    def show(self):
        curr=self.head
        while curr!=None:
            print(curr.val,end=" ")
            curr=curr.next
s1=Stack()
s1.push(3)
s1.push(5)
s1.push(6)
s1.pop()
s1.show()
print(s1.length())
print(s1.peek())

#=========================================
# Check for balanced Parenthesis
#==========================================
def isbalanced(st):
    s=Stack()
    for i in st:
        if i=='(' or i=='{' or i=='[':
            s.push(i)
        else:
            if s.length()==0:
                return False
            else:
                p={')':'(',']':'[','}':'{'}
                t=s.peek()
                if p[i]==t:
                    s.pop()
                else:
                    return False
    return s.length()==0
print(isbalanced('{}([()])'))


#=========================================
# Infix Prefix and Postfix
#==========================================
# Note:>Associavity [[^],[*,/],[+,-]]
#Example:>
    # Infix             Prefix                 Postfix
    # x+y*z             +x*yz                  xyz*+
    # (x+y)*z           *+xyz                  xy+z*

#=============================================
# Infix to Postfix Conversion
#==============================================
def intopost(st):
    a=[]
    for i in st:
        if i not in ('^','*','/','+','-','(',')'):
            print(i,end="")
        else:
            if i =='(':
                a.append('(')
            elif i==')':
                while a[-1]!='(':
                    print(a.pop(),end="")
                a.pop()
            else:
                priorty={'^':5,'*':4,'/':3,'+':2,'-':1}
                if a==[]:
                    a.append(i)
                elif a[-1]=='(' or priorty[i]>priorty[a[-1]]:
                    a.append(i)
                else:
                    while a!=[] and priorty[i]<=priorty[a[-1]]:
                        print(a.pop(),end="")
                    a.append(i)
    while a!=[]:
        print(a.pop(),end="")
    print()
intopost('a+b/c-d*e')

#=============================================
# Postfix Evaluation
#==============================================
def postev(st):
    stack=[]
    for i in st:
        if i not in ('^','*','/','+','-'):
            stack.append(i)
        else:
            p1=stack.pop()
            p2=stack.pop()
            stack.append(f'({p2}{i}{p1})')
    return stack[-1]
print(postev('123^^'))

#=============================================
# Infix to Prefix
#==============================================
def intopre(st):
    st=st[::-1]
    stack=[]
    s=""
    for i in st:
        if i not in ('^','*','/','+','-','(',')'):
            s+=i
        else:
            if i==')':
                stack.append(i)
            elif i=='(':
                while stack[-1]!=')':
                    s+=stack.pop()
                stack.pop()
            else:
                if stack==[]:
                    stack.append(i)
                else:
                    priorty={'^':5,'*':4,'/':3,'+':2,'-':1}
                    if stack[-1]==')' or priorty[i]>priorty[stack[-1]]:
                        stack.append(i)
                    else:
                        while stack!=[] and priorty[i]<=priorty[stack[-1]]:
                            s+=stack.pop()
                        stack.append(i)
    while stack!=[]:
        s+=stack.pop()
    return s[::-1]
print(intopre('x+y/z-w*u'))

#=============================================
# Prefix Evaluation
#==============================================
def prefixev(st):
    st=st[::-1]
    stack=[]
    for i in st:
        if i not in ('^','*','/','+','-'):
            stack.append(i)
        else:
            p1=stack.pop()
            p2=stack.pop()
            stack.append(f'({p2}{i}{p1})')
    return stack[-1]
print(prefixev('+*abc'))
