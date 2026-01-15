#AI generated two-sum tester.
from two_sum import two_sum

def test_two_sum():
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1], "Test case 1 failed"

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2], "Test case 2 failed"

    # Test case 3
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1], "Test case 3 failed"

    print("All test cases passed!")


test_two_sum()