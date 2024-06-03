from typing import NoReturn


def validate_input_arr(arr) -> None:
    """Validates the input array."""
    validate_empty_value(arr)
    validate_length_arr_smaller_than_3(arr)
    validate_all_elements_is_integer(arr)


def validate_empty_value(arr: list) -> NoReturn:
    """Validates that value in array not empty"""
    if arr is []:
        raise ValueError('The array must not be Empty')


def validate_length_arr_smaller_than_3(arr: list) -> NoReturn:
    """Validates that length of array is less than 3 characters"""
    if len(arr) < 3:
        raise ValueError('The array must contain more than 2 elements.')


def validate_all_elements_is_integer(arr: list) -> NoReturn:
    """Validates that all elements is integer."""
    if not all(isinstance(x, int) for x in arr):
        raise ValueError('All array elements must be integers.')
