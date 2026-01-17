#AI generated ListNode class for Add Two Numbers problem.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Non-Ai implementation of solution.
def ln2int(ln:ListNode) -> int:
    result = 0
    place = 0
    while ln.next is not None:
        result += ln.val * (10 ** place)
        ln = ln.next
        place += 1
    return result

def add_two_numbers(l1:ListNode, l2: ListNode) -> ListNode:
    num1 = ln2int(l1)
    num2 = ln2int(l2)
    sum = num1 + num2
    solution = ListNode(0)
    curr = solution
    place = 0
    while sum > 0:
        curr.val = sum % (10 ** place)
        if sum < 10:
            sum = sum / (10 ** place)
            place += 1
            curr = curr.next
        else:
            break
    return solution