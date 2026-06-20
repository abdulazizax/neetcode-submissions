# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4]

        # slow -> 1
        # fast -> 1,2
    
        # slow -> 1,2
        # fast -> 1,2,3

        # slow -> 1,2
        # fast -> 1,2,3 // if fast.next.next == Null => slow.next = fast.next

        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while n:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
