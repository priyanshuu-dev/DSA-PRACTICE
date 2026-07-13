class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(-1)
        curr=dummy
        l1=list1
        l2=list2
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1 != None:
            curr.next=l1
        else:
            curr.next=l2

        return dummy.next