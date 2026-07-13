# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        curr=head
        length=0

        while curr:
            length+=1
            curr=curr.next
        curr=head
        posn=length//2

        for i in range(posn):
            curr=curr.next
        return curr