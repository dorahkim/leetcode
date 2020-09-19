# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        # recursive
        """
        rvse = self.reverseList(head.next)
        tmp = rvse
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = head
        head.next = None
        return rvse
        """

        # iterative
        dummy = ListNode(0)
        while head is not None:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
