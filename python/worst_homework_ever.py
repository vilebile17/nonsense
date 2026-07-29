import random

solutions = []

while True:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)
    if (
        nums[0]
        + 13 * nums[1] / nums[2]
        + nums[3]
        + 12 * nums[4]
        - nums[5]
        - 11
        + nums[6] * nums[7] / nums[8]
        - 10
        == 66
    ):
        if nums not in solutions:
            solutions.append(nums)
            print(len(solutions))
