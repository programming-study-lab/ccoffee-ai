from typing import Sequence

def average(numbers: Sequence[float] | Sequence[int]) -> float:
    """Return the average of a sequence of numbers.

    Args:
        numbers (Sequence[float] | Sequence[int]): A sequence of numeric values.

    Returns:
        float: The average of the values, or 0.0 for an empty sequence.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))  # Output: 3.0
print(average([10.5, 20.5, 30.0]))  # Output: 20.333333333333332
print(average([]))  # Output: 0.0   