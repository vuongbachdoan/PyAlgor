# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 1
        size = 1
        while temp.next != None:
            size += 1
            temp = temp.next
        
        if size == n:
            head = head.next
            return head

        temp = head
        while temp.next != None:
            if count == (size - n):
                skip = temp.next
                temp.next = skip.next
                break
            temp = temp.next
            count += 1
        return head