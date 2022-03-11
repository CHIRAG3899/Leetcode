#Given the head of a linked list, rotate the list to the right by k places.

#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#Example 2:
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: 
            return head
        
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1
            
        if k % n == 0: 
            return head
        
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
            
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head