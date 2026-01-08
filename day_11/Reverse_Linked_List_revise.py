### Reverse of Linked List ###

class ListNode:
    def __init__(self, val=0,next=None):
        self.val=val
        self.next=next

def insertListNode(head,val):
    new_node = ListNode(val)
    
    if head is None:
        return new_node
    
    curr=head
    
    while curr.next:
        curr=curr.next
    curr.next=new_node
    
    return head

def Reverse_Linked_List(head:ListNode)->ListNode:
    prev=None
    curr=head
    
    while curr:
        next_node = curr.next
        curr.next=prev
        prev=curr
        curr=next_node
        
    return prev

def printLinkedList(head):
    curr=head
    
    while curr:
        print(curr.val,end=" -> ")
        curr=curr.next
    print(None)

head = None
values = [i for i in range(20)]

for i in values:
    head = insertListNode(head,i)

print("Original Linked List")
printLinkedList(head)

head=Reverse_Linked_List(head)
print("Reverse Linked List")
printLinkedList(head)