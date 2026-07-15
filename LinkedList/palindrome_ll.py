# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        middle=slow
        second_head=middle.next
        prev=None
        while second_head:
            head_next=second_head.next
            second_head.next=prev
            prev=second_head
            second_head=head_next
        
        first=head
        second=prev

        while second:
            if first.val != second.val:
                return False
            else:
                first=first.next
                second=second.next
        return True
