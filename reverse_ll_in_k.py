class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev
    
# Function to get the Kth node from
# a given position in the linked list
def getKthNode(temp, k):
    # Decrement K as we already
    # start from the 1st node
    k -= 1

    # Decrement K until it reaches
    # the desired position
    while temp is not None and k > 0:
        # Decrement k as temp progresses
        k -= 1

        # Move to the next node
        temp = temp.next

    # Return the Kth node
    return temp


# Function to reverse nodes in groups of K
def kReverse(head, k):
    # Initialize a temporary
    # node to traverse the list
    temp = head

    # Initialize a pointer to track the
    # last node of the previous group
    prevLast = None

    # Traverse through the linked list
    while temp is not None:
        # Get the Kth node of the current group
        kThNode = getKthNode(temp, k)

        # If the Kth node is NULL
        # (not a complete group)
        if kThNode is None:
            # If there was a previous group,
            # link the last node to the current node
            if prevLast:
                prevLast.next = temp

            # Exit the loop
            break

        # Store the next node
        # after the Kth node
        nextNode = kThNode.next

        # Disconnect the Kth node
        # to prepare for reversal
        kThNode.next = None

        # Reverse the nodes from
        # temp to the Kth node
        reverseLinkedList(temp)

        # Adjust the head if the reversal
        # starts from the head
        if temp == head:
            head = kThNode
        else:
            # Link the last node of the previous
            # group to the reversed group
            prevLast.next = kThNode

        # Update the pointer to the
        # last node of the previous group
        prevLast = temp

        # Move to the next group
        temp = nextNode

    # Return the head of the
    # modified linked list
    return head
