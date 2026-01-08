### Reverse of Linked List ###

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    

def ReverseList(head:ListNode)->ListNode:
    prev=None
    curr=head
    
    while curr:
        next_node=curr.next # Save Next
        curr.next=prev
        prev = curr
        curr = next_node
    return prev
    
def insertNode(head,val):
    new_node = ListNode(val)
    
    if head is None:
        return new_node
    
    curr = head
    
    while curr.next:
        curr=curr.next
    
    curr.next=new_node
    
    return head

def print_list(head):
    prev=None
    curr=head
    
    while curr:
        print(curr.val , end=" -> ")
        curr=curr.next
    print(None)
    
head=None
values =[1,2,3,4,5]
for v in values:
    head= insertNode(head, v)
    
print("Original List")
print_list(head)

print("Reverse List")
head = ReverseList(head)
print_list(head)