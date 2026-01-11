#Non-ai two-sum implementation.
def two_sum(nums : list[int], target: int) -> list[int]:
    #Code explanation:
    #declare two variables to iterate through nums.
    #while the first index is less than the length of nums:
    #if nums at the two indicies sum up to the target, return them as a solution
    #otherwise, if the second index is at the last position in the array,
    #then increase the first index by one and set the second equal to the new first index plus one
    #otherwise, just increase the second index by one
    solution = []
    indx1 = 0
    indx2 = indx1 + 1
    while indx1 != len(nums):
        if nums[indx1] + nums[indx2] == target:
            solution = [indx1, indx2]
            return solution
        else:
            if indx2+1 == len(nums):
                indx1 += 1
                indx2 = indx1 + 1
            else:
                indx2 += 1
    return solution