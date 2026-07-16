# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        l1=headA
        l2=headB
        length_A=0
        length_B=0

        while l1:
            length_A+=1
            l1=l1.next

        while l2:
            length_B+=1
            l2=l2.next
        l1=headA
        l2=headB

        if length_A>length_B:
            difference=length_A - length_B

        elif length_A<length_B:
            difference=length_B - length_A
        
        else:
            difference=0
            

        if length_A>length_B:
            for i in range(difference):
                l1=l1.next
        elif length_B>length_A:
            for i in range(difference):
                l2=l2.next
            
        while l1:
            if l1 is l2:
                return l1
            l1=l1.next
            l2=l2.next

        return None