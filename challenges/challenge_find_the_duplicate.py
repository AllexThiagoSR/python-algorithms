def find_duplicate(nums: list[int]):
    sorted_nums = sorted(nums)

    try:
        for index in range(1, len(sorted_nums)):
            if sorted_nums[index - 1] == sorted_nums[index] and not (
                sorted_nums[0] < 1 or sorted_nums[index] < 1
            ):
                return sorted_nums[index]
        return False

    except TypeError:
        return False
