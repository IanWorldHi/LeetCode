# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Faster solution with fast & slow pointer, slow one is going 1/2 speed to get middle
        head2 = head
        count = 0
        while head2 !=None:
            count+=1
            head2 = head2.next
        middle = int(count/2) +1
        #also can do count //2
        count = 0
        head2 = head
        while count<middle-2:
            head2 = head2.next
            count+=1
        #head3 = (head2.next).next
        if head2 == None or head2.next == None:
            return None
        head2.next = head2.next.next
        return head
            
        


