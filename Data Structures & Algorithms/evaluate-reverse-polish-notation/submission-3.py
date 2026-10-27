class DoublyLinkedList:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head # initially, curr and head point to the same value

        for i in range(1, len(tokens)): # building the linked list
            curr.next = DoublyLinkedList(tokens[i], prev=curr) 
            curr = curr.next

        while head is not None: # evaluating the linked list
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l/r)

                head.val = str(res)
                # Replace the operator in the current node with the calculated result.
                # Convert to string because the original tokens are stored as strings.
                # head still points to the SAME node, only its value changes.

                head.prev = head.prev.prev.prev
                # Skip the two nodes immediately before head (the operands we just used).
 

                if head.prev is not None:
                    # Check that a node exists before head.
                    # Otherwise, accessing head.prev.next would cause an error.

                    head.prev.next = head
                    # Make that previous node point FORWARDS to our current node (head).
                    # We use 'head' because it contains the calculated result.
                    # This completes the connection in BOTH directions.
                    # The two operand nodes are now bypassed.

            ans = int(head.val)
            # Store the current node's value in ans as an integer.
            # If this node was an operator, head.val now contains its calculated result.
            # ans gets updated on every iteration until the final answer is reached.

            head = head.next
            # Move head to the next node to continue traversing the linked list.
            # This does NOT change the linked list itself, only where head points.
            # If there is no next node, head becomes None and the while loop stops.
        return ans


        