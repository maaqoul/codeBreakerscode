# problem : https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
#
# i should remove the k element beginning from the end, to do that i need to make two pointers one to
# keep to traverse the list k steps
#
# pseudo algo :
#
# loop through nodes k steps
# pointertwo = node.next
# loop from pointer two to the end of list
#  pointerone = actual node.next
#
# pointerone.next = pointerone.next.next


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def removeKthNodeFromEnd(self, head, k):
        # Write your code here.
        first = head
        second = head

        for i in range(k):
            if(second.next == None):
                if (i == k-1):
                    head = head.next
                return head
            second = second.next
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next
