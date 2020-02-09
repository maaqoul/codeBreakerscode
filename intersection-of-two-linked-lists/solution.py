# problem : https://leetcode.com/problems/intersection-of-two-linked-lists/

# we need to find the node where to singly linked list intersect
# to do that we need to find the value of the node in A that's equal to the value of the node in B
# so basically we need to traverse each need and comparate them till we find a match value in both the nodes

# a pseudo algorithm would be :
#  while A has value:
#    while B has value:
#       if  A.value equal B.value
#           return value of intersection


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        values = set()
        while headA is not None:
            values.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in values:
                return headB
            headB = headB.next

        return None
