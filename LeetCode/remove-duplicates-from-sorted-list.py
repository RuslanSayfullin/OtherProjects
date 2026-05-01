# Получив начало отсортированного связанного списка, удалите все дубликаты таким образом, чтобы каждый элемент встречался только один раз. 
# Верните также отсортированный связанный список.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Пропускаем дублирующий узел
                current.next = current.next.next
            else:
                # Переходим к следующему узлу
                current = current.next

        return head


head = [1,1,2]
example = Solution()
result1 = example.deleteDuplicates(head) 
print("result1", result1)

head = [1,1,2,3,3]
example = Solution()
result2 = example.deleteDuplicates(head) 
print("result1", result2)