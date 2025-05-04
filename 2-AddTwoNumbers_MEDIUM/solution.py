# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    output_list = ListNode()

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_list = ListNode()
        currentL1Node = l1
        currentL2Node = l2
        currentOutputNode = output_list
        carry_over = 0
        while(currentL1Node is not None or currentL2Node is not None):
            if currentL2Node is None:
                currentL2Node = ListNode()
                currentL2Node.val = 0
            if currentL1Node is None:
                currentL1Node = ListNode()
                currentL1Node.val = 0
            output_val =  currentL1Node.val+currentL2Node.val+carry_over
            if(output_val >= 10):
                carry_over = 1
            else:
                carry_over = 0
            output_cleaned = int(str(output_val)[-1])
            currentOutputNode.val = output_cleaned
            if(currentL1Node.next is not None or currentL2Node.next is not None):
                currentOutputNode.next = ListNode()
                currentOutputNode = currentOutputNode.next
            else:
                if(carry_over == 1):
                    currentOutputNode.next = ListNode()
                    currentOutputNode = currentOutputNode.next
                    currentOutputNode.val = carry_over
            currentL1Node = currentL1Node.next
            currentL2Node = currentL2Node.next

            
            print(output_list)
        return output_list

        