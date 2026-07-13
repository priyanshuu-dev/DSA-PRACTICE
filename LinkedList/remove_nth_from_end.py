# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        length=0
        dummy=head
        while curr:
            length+=1
            curr=curr.next

        position=length-n
        curr=head

        if position>0:
            for i in range(position-1):
                curr=curr.next
            curr.next=curr.next.next
            return dummy
        else:
            return dummy.next
        

        

        

        






       

    






       


        
        