#AI generated ListNode class for Add Two Numbers problem.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Non-Ai implementation of solution.
def add_two_numbers(l1:ListNode, l2: ListNode) -> ListNode:
    num1 = 0
    place = 0
    while l1.next is not None:
        num1 += l1.val * (10 ** place)
        l1 = l1.next
        place += 1
    place = 0
    num2 = 0
    while l2.next is not None:
        num2 += l2.val * (10 ** place)
        l2 = l2.next
        place += 1
    sum = num1 + num2
    solution = ListNode(0)
    curr = solution
    while sum > 0:
        curr.val = sum % (10 ** place)
        sum = sum / (10 ** place)
        place -= 1
    return solution