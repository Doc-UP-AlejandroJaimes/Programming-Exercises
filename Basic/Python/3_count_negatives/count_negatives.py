def count_negatives(nums: list) -> int:
    """
    Counts the number of negative numbers in a given list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of negative numbers in the list.

    Example:
    >>> count_negatives([1, -2, -3, 4, -5])
    3
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
