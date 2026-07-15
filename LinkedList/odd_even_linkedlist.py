# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head and head.next:
            odd=head
            even=head.next
            connecting_head=head.next
            while even and even.next:
                odd.next=odd.next.next
                even.next=even.next.next

                odd=odd.next
                even=even.next

            odd.next=connecting_head

            return head

        else:
            return head
