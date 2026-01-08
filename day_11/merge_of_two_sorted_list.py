### Merged Two sorted List ###

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


def insertLinkedList(head,val):
    new_node = ListNode(val)
    
    if head is None:
        return new_node
    
    curr=head
    
    while curr.next:
        curr=curr.next
    curr.next= new_node
    
    return head

def merge_two_linked_list(l1:ListNode,l2:ListNode)->ListNode:
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val<=l2.val:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail = tail.next
    
    if l1:
        tail.next=l1
    else:
        tail.next=l2
    return dummy.next


def printListNode(head):
    curr=head
    
    while curr:
        print(curr.val, end=" -> ")
        curr=curr.next
    print(None)

l1 = [i for i in range(0,31,2)]
l2 = [i for i in range(1,30,2)]

listNode1=None
listNode2=None

for i in l1:
    listNode1=insertLinkedList(listNode1,i)

for i in l2:
    listNode2=insertLinkedList(listNode2,i)

print("Original Linked Lists are")
printListNode(listNode1)
printListNode(listNode2)

merged_list = merge_two_linked_list(listNode1,listNode2)
print("merged Two List is")
printListNode(merged_list)
