# Если задан заголовок односвязного списка, верните true, если он равен a, или false в противном случае.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        is_palindrome: bool = True

        if not head or head.next:
            is_palindrome = True
  

        # Середина списка
        middle = end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next

        if end:
            middle = middle.next

        prev = None
        curr = middle

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
        second_half_head = prev
        
        p1, p2 = head, second_half_head

        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
        
            p1 = p1.next
            p2 = p2.next
        

        return is_palindrome
    
example = Solution()
    
head = [1,2,2,1]
result1 = example.isPalindrome(head)
assert result1
print( "result1", result1)
        