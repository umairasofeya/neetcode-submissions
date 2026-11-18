# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #while curr is not null/ while curr exists
            temp = curr.next # save the next node to later set curr to this
            curr.next = prev # change the link to previous node 
            prev = curr # go to the next node by making current node its previous 
            curr = temp # and curr is now temp
        return prev 



"""
my approach:
1. because you have head, you have link to the next node and etc
2. so i guess the easiest way to be able to do it is traverse through the node, until next is None maybe for example, then once u reach the end
3. u -1 and add it into a new list? 
then copy that result into the initial list.

improving step 3
3. the only way to -1 is if u were to store the values in an array and yes that would take unnecessary space. the smarter option is to change the link in the node itself. so saving that node, but then changing it to link to the previous node, but iterate to the next node... which sounds complicated. to avoid losing track of the next nodes, we have to make a pointer called temp. the other two ptrs are curr and prev
"""
