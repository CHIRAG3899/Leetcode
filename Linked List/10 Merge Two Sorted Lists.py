#Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
#Example 1:
#Input: l1 = [1,2,4], l2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Example 2:
#Input: l1 = [], l2 = []
#Output: []
#Example 3:
#Input: l1 = [], l2 = [0]
#Output: [0]

class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        if(head2==None):
            return head1
        elif(head1==None):
            return head2
        else:
            if(head1.val<=head2.val):
                head1.next=self.mergeTwoLists(head1.next,head2)
                return head1
            else:
                head2.next=self.mergeTwoLists(head1,head2.next)
                return head2
