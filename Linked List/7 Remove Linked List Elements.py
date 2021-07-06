#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
#Example 1:
#Input: head = [1,2,6,3,4,5,6], val = 6
#Output: [1,2,3,4,5]
#Example 2:
#Input: head = [], val = 1
#Output: []
#Example 3:
#Input: head = [7,7,7,7], val = 7
#Output: []


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while(head!=None and head.val==val):
            head=head.next
        
        curr=head
        prev=ListNode()
        prev.next=curr
        while(curr!=None):
            if(curr.val==val):
                prev.next=curr.next
                curr=curr.next
            else:
                curr=curr.next
                prev=prev.next
        return head
