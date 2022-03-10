#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example 1:
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp =l1
        prev  = None
        while(l1 and l2):
            val   =l1.val+l2.val+carry
            carry =val//10
            l1.val =val%10
            prev= l1
            l1,l2 =l1.next,l2.next
        prev.next = l1 or l2
        while(l1):
            val  =l1.val+carry
            carry  =val//10
            prev = l1
            l1.val =val%10
            l1 = l1.next
            if carry ==0:
                return temp
        while(l2):
            val  =l2.val+carry
            carry  =val//10
            l2.val =val%10
            prev= l2
            l2 = l2.next
            if carry ==0:
                return temp
        if carry:
            prev.next  = ListNode(carry)
        return temp