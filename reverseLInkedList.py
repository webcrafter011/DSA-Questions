class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
printLinkedList(head)

reversed_head = reverseLinkedList(head)

print("Reversed Linked List:")
printLinkedList(reversed_head)