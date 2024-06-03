import json
import os

from equilibrium_index_finder.validations.validation_input_array import validate_input_arr

_NOT_EQUUILIBRIUM_INDEX = -1


def save_result_to_json(result_data: int, dst_filepath: str) -> None:
    """Saves result to json.

    Args:
        result_data: Equilibrium index.
        dst_filepath: Path to destination file.

    """
    directory = os.path.dirname(dst_filepath)
    os.makedirs(directory, exist_ok=True)

    with open(dst_filepath, 'w') as f:
        json.dump({'equilibrium_index': result_data}, f, indent=2)


def find_index(arr: list) -> int:
    """Algorithm to find the equilibrium index in list of integers

    Args:
        arr: Input list integers.

    Returns:
        Equilibrium index, or (-1) if it's not in the list.

    """
    validate_input_arr(arr)
    total_sum = sum(arr)
    left_sum = 0

    for index in range(len(arr)):
        total_sum -= arr[index]

        if left_sum == total_sum:
            return index

        left_sum += arr[index]

    return _NOT_EQUUILIBRIUM_INDEX
