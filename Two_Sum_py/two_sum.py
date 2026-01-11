#Non-ai two-sum implementation.
def two_sum(nums : list[int], target: int) -> list[int]:
    indx1 = 0
    indx2 = 1
    solution = []
    while indx1 < len(nums):
        if nums[indx1] + nums[indx2] == target:
            solution.append(indx1)
            solution.append(indx2)
            indx1 += 1
            indx2 = indx1 + 1
        else:
            if indx2 < len(nums):
                indx2 += 1
            else:
                break
    return solution