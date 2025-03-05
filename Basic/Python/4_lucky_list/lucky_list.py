def has_lucky_number(nums: list) -> bool:
    """
    Checks if a given list contains at least one "lucky number" (a multiple of 7).

    Parameters:
    nums (list): A list of integers.

    Returns:
    bool: True if at least one number in the list is a multiple of 7, False otherwise.

    Example:
    >>> has_lucky_number([3, 14, 10, 21])
    True
    >>> has_lucky_number([1, 2, 3, 5])
    False
    """
    has_lucky = False
    if len(nums) == 0:
        return has_lucky
    else:
        for num in nums:
            if num % 7 == 0:
                has_lucky = True
                break
    return has_lucky
