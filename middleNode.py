class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middle_node(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    mid = count // 2
    current = head
    for _ in range(mid):
        current = current.next
    return current 