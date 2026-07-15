# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle=slow

        new_head=middle.next
        middle.next=None
        prev=None
        while new_head:
            new_head_next=new_head.next
            new_head.next=prev
            prev=new_head
            new_head=new_head_next
        first=head
        second=prev

        while second:
            first_next=first.next
            second_next=second.next
            first.next=second
            second.next=first_next
            first=first_next
            second=second_next