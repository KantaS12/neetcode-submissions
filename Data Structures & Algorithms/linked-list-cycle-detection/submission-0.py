#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # We have to determine if the tail node is pointing at index == -1 (not cycling) or index == 1 (cycling)

        fast = head
        slow = head

        while fast and fast.next:
            # move once
            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True

        return False


        