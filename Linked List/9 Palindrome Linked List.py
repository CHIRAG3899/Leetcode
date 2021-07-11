#Given the head of a singly linked list, return true if it is a palindrome.
#Example 1:
#Input: head = [1,2,2,1]
#Output: true
#Example 2:
#Input: head = [1,2]
#Output: false

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = 0
        slow=fast = head

        while fast and fast.next:
            num = num*10+slow.val
            slow = slow.next
            fast = fast.next.next

        # At this point I have half the number in num
        if fast:  # mean list has odd count nodes, need change to next. This is imp
            slow = slow.next
            
        while slow:
            last = num%10
            if slow.val != last:
                return False
            num = num //10
            slow = slow.next
        return True
