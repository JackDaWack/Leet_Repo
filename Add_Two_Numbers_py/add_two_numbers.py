#AI generated ListNode class for Add Two Numbers problem.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Non-Ai implementation of solution.
#Helper function that converts list nodes to numbers.
def ln2int(ln:ListNode) -> int:
    result = 0
    place = 0
    while ln is not None:
        result += ln.val * (10 ** place)
        ln = ln.next
        place += 1
    return result

#Main solution.
def add_two_numbers(l1:ListNode, l2: ListNode) -> ListNode:
    #Logic: 
    # Convert the list nodes to ints and get their sum.
    # Create a solution variable with empty list nodes and let curr be the reference point.
    # While the sum value is greater than 0, take the remainder of the sum value over 10 and set it as the node value.
    # Create a new empty node and set curr over to that node.
    # if the remaining value is less than 10, set the new curr value to the sum and set sum equal to 0.
    # Return the final solution.
    num1 = ln2int(l1)
    num2 = ln2int(l2)
    sum = num1 + num2
    solution = ListNode(0)
    curr = solution
    while sum > 0:
        curr.val = sum % 10
        sum = sum // 10
        curr.next = ListNode(0)
        curr = curr.next
        if sum < 10:
            curr.val = sum
            sum = 0
    return solution