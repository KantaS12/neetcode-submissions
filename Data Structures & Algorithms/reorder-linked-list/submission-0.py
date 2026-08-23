# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle of the linkedlist without knowing the length of the linkedlist

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Now we know that slow is the middle node
        # Now we're going to reverse the second half

        # The starting of the second half is after the middle node
        current = slow.next

        # Cut off the first list so we can add it to that after we reverse it
        slow.next = None

        # Set a previous for the second list for reversal
        prev = None

        while current:
            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        # Now we reversed the second linked list

        # Now we have to re attach it to the first but it goes from 1st list -> 2nd list -> etc..

        first_p = head
        second_p = prev


        while second_p:

            first_next = first_p.next
            second_next = second_p.next

            first_p.next = second_p
            second_p.next = first_next

            first_p = first_next
            second_p = second_next

        return None







