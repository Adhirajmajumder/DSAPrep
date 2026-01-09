#### Linked List Nth node deleteion ####

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def delete_Nth_Node(head,k):
    dummy = ListNode(0)
    dummy.next = head
    
    fast=slow=dummy
    
    for _ in range(k):
        fast=fast.next
        
    while fast.next:
        slow=slow.next
        fast=fast.next
    
    slow.next=slow.next.next
    
    return dummy.next
    

def insertLinkedList(head, val):
    new_node = ListNode(val)
    
    curr=head
    
    if head is None:
        return new_node
    
    while curr.next:
        curr=curr.next
    
    curr.next=new_node
    
    return head

def printLinkedList(head:ListNode):
    curr=head
    
    while curr:
        print(curr.val, end=" -> ")
        curr=curr.next
    print(None)

listVal = [2,3,4,5,6,7,8,9]

listHead = ListNode(1)

for i in listVal:
    
    head = insertLinkedList(listHead,i)

print("Print Linked List before deletion")
printLinkedList(head)
deleted_node=4
head = delete_Nth_Node(head,deleted_node)
print(f"Print Linked List after deleteion {deleted_node} from end")
printLinkedList(head)