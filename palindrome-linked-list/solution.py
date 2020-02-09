# problem : https://leetcode.com/problems/palindrome-linked-list/
# in this problem i need to check if a given list is a palindrome, to do so, i ll push node values to an array
# and compare the popped item of the array to the actual value of the node if they match i ll return
# true if not -> false
#
#
# psudo algoritm :
# var stack of type array
# while node is not none
# stack <- node.value
# while node is not none
# check if stack.pop() == node.value#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        current = head
        while current is not None:
            stack.append(current.val)
            current = current.next
        current = head
        while current is not None:
            value = stack.pop()
            if current.val != value:
                return False
            current = current.next
        return True
