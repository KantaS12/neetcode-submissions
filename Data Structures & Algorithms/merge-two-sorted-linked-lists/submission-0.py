# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Make a third LinkedList so we can add into it
        # Create a tail pointer at the end of the third
        # Compare both and if one is smaller then add it to the tail.next
        # Move the tail forward
        # Move the Linkedlist forward that is the smaller

        list3 = ListNode()

        tail = list3

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next

            elif list1.val > list2.val:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        # strays for list 1 and list 2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return list3.next
            

            
            



