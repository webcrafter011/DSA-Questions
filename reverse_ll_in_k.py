class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverseLinkedList(head):
    temp = head
    prev = None
    
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev
    
def getKthNode(temp, k):
    k -= 1
    while temp is not None and k > 0:
        k -= 1
        temp = temp.next
    return temp

def kReverse(head, k):
    temp = head
    prevLast = None

    while temp is not None:
        kThNode = getKthNode(temp, k)

        if kThNode is None:
            if prevLast:
                prevLast.next = temp
            break

        nextNode = kThNode.next
        kThNode.next = None
        reverseLinkedList(temp)

        if temp == head:
            head = kThNode
        else:
            prevLast.next = kThNode

        prevLast = temp
        temp = nextNode

    return head
