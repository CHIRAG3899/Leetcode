#You are given the head of a linked list, and an integer k.
#
#Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
#
#Example 1:
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [1,4,3,2,5]
#Example 2:
#
#Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
#Output: [7,9,6,6,8,7,3,0,9,5]

class Solution:
    def swapNodes(self, head, k):
        n = 0
        beg = head
        while beg:
            if n == k-1: l = beg
            beg = beg.next
            n += 1
        
        r = head
        for m in range(n-k):
            r = r.next
                
        l.val, r.val = r.val, l.val
        return head