#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#Example 1:
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]
#Example 2:
#Input: head = [1], n = 1
#Output: []
#Example 3:
#Input: head = [1,2], n = 1
#Output: [1]

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first_ptr = findNthNode(head, n).next
        second_ptr = head
        while first_ptr and first_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # This implies len(ListNode)==n, so Head node should be removed
        if first_ptr is None:
            return head.next
        else:
            removeNodeAfter(second_ptr)
        return head


def findNthNode(head: ListNode, n: int) -> ListNode:
    ptr = head
    for i in range(n - 1):
        ptr = ptr.next
    return ptr


def removeNodeAfter(node) -> None:
    if node.next:
        node.next = node.next.next
