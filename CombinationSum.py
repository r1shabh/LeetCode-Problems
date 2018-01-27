__author__ = 'rishabh anand'


def combinationSum(candidates, target):
    candidates.sort()
    return helper(candidates, target, [], [], 0)


def helper(candidates, target, solution, solutions, i):
    if target == 0:
        if len(solution) > 0:
            solutions.append(solution[:])
        return solutions
    elif target < 0:
        target += solution.pop()
    while i < len(candidates) and target - candidates[i] >= 0:
        solution.append(candidates[i])
        helper(candidates, target-solution[-1], solution, solutions, i)
        i += 1
        solution.pop()
    return solutions


print combinationSum([2, 3, 6, 7], 7)
print combinationSum([1, 2, 3], 5)
print combinationSum([1, 2], 0)
print combinationSum([8, 7, 4, 3], 11)
