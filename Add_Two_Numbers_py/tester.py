import add_two_numbers

#AI generated Add Two Numbers tester.

def test_add_two_numbers():
    # Test case 1
    l1 = add_two_numbers.ListNode(2, add_two_numbers.ListNode(4, add_two_numbers.ListNode(3)))
    l2 = add_two_numbers.ListNode(5, add_two_numbers.ListNode(6, add_two_numbers.ListNode(4)))
    result = add_two_numbers.add_two_numbers(l1, l2)
    expected = [7, 0, 8]
    for val in expected:
        assert result.val == val, "Test case 1 failed"
        result = result.next

    # Test case 2
    l1 = add_two_numbers.ListNode(0)
    l2 = add_two_numbers.ListNode(0)
    result = add_two_numbers.add_two_numbers(l1, l2)
    expected = [0]
    for val in expected:
        assert result.val == val, "Test case 2 failed"
        result = result.next

    # Test case 3
    l1 = add_two_numbers.ListNode(9, add_two_numbers.ListNode(9, add_two_numbers.ListNode(9)))
    l2 = add_two_numbers.ListNode(1)
    result = add_two_numbers.add_two_numbers(l1, l2)
    expected = [0, 0, 0, 1]
    for val in expected:
        assert result.val == val, "Test case 3 failed"
        result = result.next
    print("All test cases passed!")

test_add_two_numbers()