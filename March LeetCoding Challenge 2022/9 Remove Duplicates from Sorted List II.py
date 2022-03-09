#Given the head of a sorted linked list, delete all nodes that have duplicate
#numbers, leaving only distinct numbers from the original list. Return the
#linked list sorted as well.
#Example 1:
#Input: head = [1,2,3,3,4,4,5]
#Output: [1,2,5]
#Example 2:
#Input: head = [1,1,1,2,3]
#Output: [2,3]


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = head, dummy
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            else:
                slow.next = fast.next
                fast = slow.next
                
        return dummy.next
