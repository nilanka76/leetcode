# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val,
# and return the new head.
# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        temp = ListNode(next = head)     
        currentNode = temp
        previousNode = currentNode
        if currentNode == None:
            return 
        while currentNode:
            if currentNode.val == val:  
                previousNode.next = currentNode.next
            else:
                previousNode = currentNode
            currentNode = currentNode.next
        return temp.next

solution = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
 
list2 = solution.removeElements(list1 , 2)
while list2:
    print(list2.val, end =" ")
    list2 = list2.next
