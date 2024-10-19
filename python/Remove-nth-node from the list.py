class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
  
    for _ in range(n + 1):
        first = first.next
  
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next

    return dummy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

n = 2
new_head = remove_nth_from_end(head, n)
current = new_head
while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
