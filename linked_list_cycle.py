# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head) -> bool:
        # temp = head
        # hmap = {}
        # while temp:
        #     if temp not in hmap:
        #         hmap[temp] = 1
        #     else:
        #         return True
        #     temp = temp.next
        # return False

        # Floyd's Tortois and Hare algo:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

solution = Solution()
list1 = ListNode(3)
list1.next = ListNode(2)
list1.next.next = ListNode(0)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = list1

print(solution.hasCycle(list1))